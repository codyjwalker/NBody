/* -----------------------------------------------------------------------------
 *
 * File:          sequential.c
 * Author:        Cody Walker
 * Class:         CSC 422 Parallel & Distributed Programming
 * Project:       Parallel Project 1 - n-Bodies and Collisions
 * Description:   A sequential implementation of a simulation of the n-body
 *                gravitational problem.
 * Created:       10 October 2018
 * Updated:       13 June 2019
 *
 * -------------------------------------------------------------------------- */


// TODO:    PEEP DISTANCE STRUCTURE!
// TODO:    change pow(x) to x * x wherever applicable.
// TODO:    MORE SIMILAR CHUNKS! i.e. (x2 - x1)^2 etc.


#include "sequential.h"

#define NUM_BODIES      50
#define TIMESTEPS       300
#define ENABLE_GUI      1
#define BODY_RADIUS     20
#define BODY_MASS       1000000000

int pdb = 1;


/* -------------------------------------------------------------------------- */
/* ----------------------------- Functions ---------------------------------- */
/* -------------------------------------------------------------------------- */



/* -----------------------------------------------------------------------------
 * Routine:     init
 * Description: Initializes global variables, setting them to be any user-
 *              supplied values if appropriate.
 * Arguments:   argv1 - number of bodies
 *              argv2 - radius of each body
 *              argv3 - number of time steps
 *              argv4 - 1 to enable output for gui, 0 otherwise
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void init(int argc, char *argv[])
{
  int i;

  // Initialize global values.
  num_bodies = NUM_BODIES;
  body_radius = BODY_RADIUS;
  timesteps = TIMESTEPS;
  enable_gui = ENABLE_GUI;

  body_mass = BODY_MASS;
  file = NULL;
  secs = 0;
  usecs = 0;

  // Pull values from arguments.
//  num_bodies = atoi(argv[1]);
//  body_radius = atoi(argv[2]);
//  timesteps = atoi(argv[3]);
//  enable_gui = atoi(argv[4]);

  // Open file.
  file = fopen("gui_input.txt", "w");

  // Write num_bodies, body_radius, & timesteps to file for GUI.
  if (fprintf(file, "%d ", num_bodies) == EOF)
  {
    error("ERROR!!! init(): PROBLEM WITH fprintf()");
  }
  if (fprintf(file, "%d ", body_radius) == EOF)
  {
    error("ERROR!!! init(): PROBLEM WITH fprintf()");
  }
  if (fprintf(file, "%d ", timesteps) == EOF)
  {
    error("ERROR!!! init(): PROBLEM WITH fprintf()");
  }

  // Set value for universal gravitational constant.
  grav_const = 6674.08;   // Scaled a bit so units are easier to work with.
  special_g = 2 * grav_const * body_mass;



  int randx = 0;
  int randy = 0;


  // Initialize positions.
  position = malloc(num_bodies * sizeof(vector *));
  for (i = 0; i < num_bodies; i++)
  {
    position[i] = malloc(sizeof(vector));
    // ACTUALLY INITIALIZE THEM SOMEHWERE USEFUL


    position[i]->x = i * 100;
    position[i]->y = i * 100;

    randx = rand() % 100;
    randy = rand() % 100;

    position[i]->x += randx;
    position[i]->y += randy;

 }

  // Initialize velocities.
  velocity = malloc(num_bodies * sizeof(vector *));
  for (i = 0; i < num_bodies; i++)
  {
    velocity[i] = malloc(sizeof(vector));
    velocity[i]->x = 0;
    velocity[i]->y = 0;
  }

  // Initialize forces.
  force = malloc(num_bodies * sizeof(vector *));
  for (i = 0; i < num_bodies; i++)
  {
    force[i] = malloc(sizeof(vector));
    force[i]->x = 0;
    force[i]->y = 0;
  }

  // Initialize collision queue.
  collisions.size = 0;
  collisions.head = NULL;
  collisions.tail = NULL;

  return;
} /* END init() */


/* -----------------------------------------------------------------------------
 * Routine:     terminate
 * Description: Cleans up all allocated memory.
 * Arguments:   None.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void terminate(void)
{
  int i;

  // Retrieve values and print.
  secs = (end_tv.tv_sec - start_tv.tv_sec);
  usecs = (end_tv.tv_usec - start_tv.tv_usec);
  if (usecs < 0)
  {
    secs = secs - 1;
    usecs = usecs + 1000000;
  }

  printf("\n\nSIMULATION TOOK %ld.%ld SECONDS.\n\n", secs, usecs);

  // Free position array.
  for (i = 0; i < num_bodies; i++)
  {
    free(position[i]);
  }
  free(position);

  // Free velocity array.
  for (i = 0; i < num_bodies; i++)
  {
    free(velocity[i]);
  }
  free(velocity);

  // Free force array.
  for (i = 0; i < num_bodies; i++)
  {
    free(force[i]);
  }
  free(force);

  // Close file.
  fclose(file);

  return;
} /* END terminate() */


/* -----------------------------------------------------------------------------
 * Routine:     calculate_forces
 * Description: For each body, calculates the net-force acting upon it from all
 *              the other bodies in the simulation in the current timeframe.
 *              The function does not move any of the bodies, and merely does
 *              the calculations for all the forces at the current moment in
 *              time.
 * Arguments:   None.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void calculate_forces(void)
{
  int i, j;
  double distance = 0.0;
  double magnitude = 0.0;
  double x_chunk = 0.0;
  double y_chunk = 0.0;
  double mag_over_dist = 0.0;
  vector direction;
  direction.x = 0.0;
  direction.y = 0.0;

  for (i = 0; i < num_bodies - 1; i++)
  {
    // Start j at i + 1 since we save the force to BOTH bodies each iteration.
    for (j = i + 1; j < num_bodies; j++)
    {
      // Calculate distance between current pair of bodies.
//      distance = sqrt(pow((position[i]->x - position[j]->x), 2) +
//          pow((position[i]->y - position[j]->y), 2));
      distance = sqrt(((position[i]->x - position[j]->x) * (position[i]->x -
                  position[j]->x)) + ((position[i]->y - position[j]->y) *
                  (position[i]->y - position[j]->y)));
      // Calculate magnitude of gravitational force between pair of bodies.
      magnitude = special_g / (distance * distance);
      direction.x = position[j]->x - position[i]->x;
      direction.y = position[j]->y - position[i]->y;
      // Precompute some chunks to lessen total # of computations.
      mag_over_dist = (magnitude / distance);
      x_chunk = (mag_over_dist * direction.x);
      y_chunk = (mag_over_dist * direction.y);
      // Save both forces to cut calculations in half.
      force[i]->x = force[i]->x + x_chunk;
      force[j]->x = force[j]->x - x_chunk;
      force[i]->y = force[i]->y + y_chunk;
      force[j]->y = force[j]->y - y_chunk;
    }
  }
  return;
} /* END calculate_forces() */


/* -----------------------------------------------------------------------------
 * Routine:     move_bodies
 * Description: For each body, determines first its new velocity as a result of
 *              the net-force acting upon it, and then its new position as a
 *              result of its new velocity.
 * Arguments:   None.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void move_bodies(void)
{
  int i;
  vector delta_v, delta_p;
  delta_v.x = 0.0;
  delta_v.y = 0.0;
  delta_p.x = 0.0;
  delta_p.y = 0.0;

  for (i = 0; i < num_bodies; i++)
  {
    // Calculate change in velocity resulting from net force on current obj.
    delta_v.x = force[i]->x / body_mass;
    delta_v.y = force[i]->y / body_mass;
    // Calculate change in position resulting from current object's velocity.
    delta_p.x = velocity[i]->x + (delta_v.x * 0.5);
    delta_p.y = velocity[i]->y + (delta_v.y * 0.5);
    // Store current object's new velocity.
    velocity[i]->x = velocity[i]->x + delta_v.x;
    velocity[i]->y = velocity[i]->y + delta_v.y;
    // Store current object's new position.
    position[i]->x = position[i]->x + delta_p.x;
    position[i]->y = position[i]->y + delta_p.y;
    // Reset force vector to prepare for next time move_bodies() is called.
    force[i]->x = 0.0;
    force[i]->y = 0.0;
  }
  return;
} /* END move_bodies() */


/* -----------------------------------------------------------------------------
 * Routine:     collisions_detected
 * Description: Checks the current state of the simulation, and determines
 *              whether or not the previous movement calculation has caused any
 *              collisions to occur.
 * Arguments:   None.
 * Returns:     1 if any collisions have occured, 0 otherwise.
 * -------------------------------------------------------------------------- */
int collisions_detected(void)
{
  int i, j;
  int collision = 0;  // Boolean representing if collision occured.
  double distance = 0.0;

  for (i = 0; i < num_bodies - 1; i++)
  {
    for (j = i + 1; j < num_bodies; j++)
    {
        // TODO: SPEED THIS SHIT UP MAYBE DISTANCE STRUCTURE??????
      // Calculate distance between current pair of bodies.
      distance = sqrt(pow((position[i]->x - position[j]->x), 2) +
          pow((position[i]->y - position[j]->y), 2));
      // Determine if bodies are currently "overlapping".
      if (distance < (2 * body_radius))
      {
        if (pdb) printf("\n\n\nCOLLISION!!!!!!!\n\n\n");
        // Mark that these two objects in particular collided.
        add_collision(i, j);
        collision = 1;
      }
    }
  }
  // Returns TRUE if collision happened, FALSE otherwise.
  return collision;
} /* END collisions_detected() */


/* -----------------------------------------------------------------------------
 * Routine:     resolve_collisions
 * Description: Called when two or more objects are in a "state of collision"
 *              to properly determine their new velocities and positions
 *              resulting from them colliding.  Without this method, not only
 *              would objects pass through eachother, but because the
 *              magnitude of the force of gravity becomes exponentially larger
 *              the closer together bodies get, the bodies would become under
 *              tremendous force and fly off at comical speeds in the direction
 *              they were just heading.  Very important function.
 *              NOTE:
 *              THE PROCEDURES USED TO CALCULATE THE FINAL VELOCITIES OF THE
 *              OBJECTS ARE TAKEN FROM DR. HOMER'S HANDOUT WHICH IS BADED ON
 *              "2-Dimensional Elastic Collisions Without Trigonometry" by
 *              Chad Bercheck, AND IS NOT MY OWN ORIGINAL MATERIAL.
 * Arguments:   None.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void resolve_collisions(void)
{
  c_node curr;          // Collision object to extract indices from.
  int body1 = -1;       // Index of first body involved in the collision.
  int body2 = -1;       // Index of second body involved in the collision.
  double x1 = 0.0;      // Body 1 initial x position.
  double y1 = 0.0;      // Body 1 initial y position.
  double x2 = 0.0;      // Body 2 initial x position.
  double y2 = 0.0;      // Body 2 initial y position.
  double v1x = 0.0;     // Body 1 initial x velocity.
  double v1y = 0.0;     // Body 1 initial y velocity.
  double v2x = 0.0;     // Body 2 initial x velocity.
  double v2y = 0.0;     // Body 2 initial y velocity.
  double v1fx = 0.0;    // Body 1 final x velocity.
  double v1fy = 0.0;    // Body 1 final y velocity.
  double v2fx = 0.0;    // Body 2 final x velocity.
  double v2fy = 0.0;    // Body 2 final y velocity.
  // Used to speed up computation.
  double denom = 0.0;
  double chunk1 = 0.0;
  double chunk2 = 0.0;
  double chunk3 = 0.0;
  double chunk4 = 0.0;

    // TODO: MORE SIMILAR CHUNKS!!! i.e. (x2 - x1)^2 etc.

  // Handle every collision that occured in current timestep.
  while (collisions.size > 0)
  {
    // First, get the two bodies involved in current collision.
    curr = pop_collision();
    body1 = curr.a;
    body2 = curr.b;

    // Extract information about velocities and positions of bodies.
    x1 = position[body1]->x;
    y1 = position[body1]->y;
    x2 = position[body2]->x;
    y2 = position[body2]->y;
    v1x = velocity[body1]->x;
    v1y = velocity[body1]->y;
    v2x = velocity[body2]->x;
    v2y = velocity[body2]->y;

    // Precompute similar "chunks" used in all equations to reduce computations.
//    denom = (pow((x2 - x1), 2) + pow((y2 - y1), 2));
    denom = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1));
    chunk1 = (v1y * (x2 - x1) * (y2 - y1));
    chunk2 = (v2y * (x2 - x1) * (y2 - y1));
    chunk3 = (v1x * (y2 - y1) * (x2 - x1));
    chunk4 = (v2x * (x2 - x1) * (y2 - y1));

    // Determine final x velocity of first body.
//    v1fx = (v2x * pow((x2 - x1), 2));
    v1fx = v2x * (x2 - x1) * (x2 - x1);
    v1fx = v1fx + chunk2;
//    v1fx = v1fx + (v1x * pow((y2 - y1), 2));
    v1fx = v1fx + (v1x * (y2 - y1) * (y2 - y1));
    v1fx = v1fx - chunk1;
    v1fx = v1fx / denom;

    // Determine final y velocity of first body.
    v1fy = chunk4;
//    v1fy = v1fy + (v2y * pow((y2 - y1), 2));
    v1fy = v1fy + (v2y * (y2 - y1) * (y2 - y1));
    v1fy = v1fy - chunk3;
//    v1fy = v1fy + (v1y * pow((x2 - x1), 2));
    v1fy = v1fy + (v1y * (x2 - x1) * (x2 - x1));
    v1fy = v1fy / denom;

    // Determine final x velocity of second body.
//    v2fx = (v1x * pow((x2 - x1), 2));
    v2fx = v1x * (x2 - x1) * (x2 - x1);
    v2fx = v2fx + chunk1;
//    v2fx = v2fx + (v2x * pow((y2 - y1), 2));
    v2fx = v2fx + (v2x * (y2 - y1) * (y2 - y1));
    v2fx = v2fx - chunk2;
    v2fx = v2fx / denom;

    // Determine final y velocity of second body.
    v2fy = chunk3;
//    v2fy = v2fy + (v1y * pow((y2 - y1), 2));
    v2fy = v2fy + (v1y * (y2 - y1) * (y2 - y1));
    v2fy = v2fy - chunk4;
//    v2fy = v2fy + (v2y * pow((x2 - x1), 2));
    v2fy = v2fy + (v2y * (x2 - x1) * (x2 - x1));
    v2fy = v2fy / denom;

    // Determine final positions of bodies.
    position[body1]->x = position[body1]->x + v1fx;
    position[body1]->y = position[body1]->y + v1fy;
    position[body2]->x = position[body2]->x + v2fx;
    position[body2]->y = position[body2]->y + v2fy;

    // Copy new velocities into global arrays.
    velocity[body1]->x = v1fx;
    velocity[body1]->y = v1fy;
    velocity[body2]->x = v2fx;
    velocity[body2]->y = v2fy;
  }
  return;
} /* END resolve_collisions() */


/* -----------------------------------------------------------------------------
 * Routine:     export_positions
 * Description: Writes the information contained inside the position array at
 *              the current timeframe to a .txt file for a GUI to read and
 *              use to generate a visualization of the simulation.
 * Arguments:   None.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void export_positions(void)
{
  int i;

  for (i = 0; i < num_bodies; i++)
  {
    if (fprintf(file, "%lf ", position[i]->x) == EOF)
    {
      error("ERROR!!! export_positions(): PROBLEM WITH fprintf()");
    }
    if (fprintf(file, "%lf ", position[i]->y) == EOF)
    {
      error("ERROR!!! export_positions(): PROBLEM WITH fprintf()");
    }
  }
  return;
} /* END export_positions() */


/* -----------------------------------------------------------------------------
 * Routine:     main
 * Description: Doesn't do much, just calls methods to do all the work instead.
 *              Records system time before and after doing the work however to
 *              be used for measurement of execution time.
 * Arguments:   argv1 - number of bodies
 *              argv2 - radius of each body
 *              argv3 - number of time steps
 *              argv4 - 1 to enable output for gui, 0 otherwise
 *              argv5 - number of dimensions to run simulation in (2 or 3)
 * Returns:     Appropriate exit status of program.
 * -------------------------------------------------------------------------- */
int main(int argc, char *argv[])
{
  int i;

  init(argc, argv);

  if (pdb) print_coordinates();

  // Record system's time immediately prior to running simulation.
  gettimeofday(&start_tv, NULL);

  // Run simulation for # timesteps that user requested.
  for (i = 0; i < timesteps; i++)
  {
    // Calculate net force acting on each body.
    calculate_forces();

    // Move bodies appropriately based upon the net force acting on them.
    move_bodies();

    // Check for collisions and resolve any that are found.
    if (collisions_detected())
    {
      resolve_collisions();
    }

    // If print debug variable turned on, print to stdout.
    if (pdb) print_coordinates();

    // If GUI mode enabled write positions to file.
    if (enable_gui) export_positions();
  }

  // Record system's time immediately upon finishing simulation.
  gettimeofday(&end_tv, NULL);

  terminate();

  exit(EXIT_SUCCESS);
} /* END main() */


/* -----------------------------------------------------------------------------
 * Routine:     routine
 * Description: description
 * Arguments:   args
 * Returns:     retval
 * -------------------------------------------------------------------------- */

/* END sequential.c */

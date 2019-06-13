/* -----------------------------------------------------------------------------
 *
 * File:          sequential.h
 * Author:        Cody Walker
 * Class:         CSC 422 Parallel & Distributed Programming
 * Project:       Parallel Project 1 - n-Bodies and Collisions
 * Description:   Header file for the sequential implementation of the n-body
 *                gravitational simulation.
 * Created:       10 October 2018
 * Updated:       7 November 2018
 *
 * -------------------------------------------------------------------------- */


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>


/* -------------------------------------------------------------------------- */
/* ------------------------------ Typedefs ---------------------------------- */
/* -------------------------------------------------------------------------- */


typedef struct vector vector;
typedef struct c_node c_node;
typedef struct c_queue c_queue;


/* -------------------------------------------------------------------------- */
/* ------------------------------ Prototypes -------------------------------- */
/* -------------------------------------------------------------------------- */


extern void init(int argc, char *argv[]);
extern void terminate(void);
extern void calculate_forces(void);
extern void move_bodies(void);
extern int collisions_detected(void);
extern void resolve_collisions(void);
extern void export_positions(void);


/* -------------------------------------------------------------------------- */
/* ------------------------------ Structures -------------------------------- */
/* -------------------------------------------------------------------------- */


struct vector
{
    double x;
    double y;
};

struct c_node
{
    int a;
    int b;
    c_node *next;
};

struct c_queue
{
    int size;
    c_node *head;
    c_node *tail;
};


/* -------------------------------------------------------------------------- */
/* ------------------------------ Globals ----------------------------------- */
/* -------------------------------------------------------------------------- */


int num_bodies;           // Number of bodies in simulation.
int body_radius;          // Radius of each body in simulation.
int timesteps;            // Number of timesteps to run in simulation.
int body_mass;            // Mass of each body in simulation.
int enable_gui;           // 1 to enable output for GUI, 0 otherwise.
int num_dimensions;       // Number of dimensions to run simulation in.

double grav_const;        // Set to 6.67408.
double special_g;         // 2*grav_const*body_mass to reduce # of computations.

FILE *file;               // Pointer to file where position results written to.

long int secs;            // Number of seconds simulation takes to run.
long int usecs;           // Number of microseconds simulation takes to run.
struct timeval start_tv;  // Current system time upon start of simulation.
struct timeval end_tv;    // Current system time upon end of simulation.

vector **position;        // Array of positions of the bodies.
vector **velocity;        // Array of velocities of the bodies.
vector **force;           // Array of net forces acting upon each of the bodies.

c_queue collisions;       // List of collisions that occurred in curr timestep.


/* -------------------------------------------------------------------------- */
/* ------------------------------ Functions --------------------------------- */
/* -------------------------------------------------------------------------- */


/* -----------------------------------------------------------------------------
 * Routine:     add_collision
 * Description: Adds a "collision node" to the queue.  A collision node
 *              contains nothing more than two integers representing the IDs of
 *              the two bodies in the collision and a pointer to the next node
 *              in the queue.
 * Arguments:   a & b - IDs of the two bodies involved in the collision.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void add_collision(int a, int b)
{
    // No existing collisions.
    if (collisions.head == NULL)
    {
        collisions.head = malloc(sizeof(c_node));
        collisions.head->a = a;
        collisions.head->b = b;
        collisions.head->next = NULL;

        collisions.tail = collisions.head;
    }
    // Existing collisions, add to end of queue.
    else
    {
        // Walk down to end of queue for proper insertion.
        c_node *walker;
        walker = collisions.head;
        while (walker->next != NULL)
        {
            walker = walker->next;
        }
        // Walker now pointing to last item in queueue.
        // Add new collision to end of queue.
        walker->next = malloc(sizeof(c_node));
        walker->next->a = a;
        walker->next->b = b;
        walker->next->next = NULL;

    collisions.tail = walker->next;
  }
  collisions.size++;
  return;
} /* END add_collision() */


/* -----------------------------------------------------------------------------
 * Routine:     pop_collision
 * Description: Removes the first node on the collision queue and returns
 *              that node.
 * Arguments:   None.
 * Returns:     A copy of the node just removed upon invokation.
 * -------------------------------------------------------------------------- */
c_node pop_collision(void)
{
  c_node result;

  if (collisions.head == NULL)
  {
    fprintf(stderr, "\nERROR!!! pop_collision(): NO NODES TO REMOVE!!\n");
    exit(EXIT_FAILURE);
  }

  result.a = collisions.head->a;
  result.b = collisions.head->b;

  collisions.head = collisions.head->next;
  if (collisions.size == 1) collisions.tail = NULL;

  collisions.size--;
  return result;
} /* END pop_collision() */


/* -----------------------------------------------------------------------------
 * Routine:     print_collisions
 * Description: Prints out the nodes and their contents that are in the
 *              collision queue upon calling.
 * Arguments:   None.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void print_collisions(void)
{
  c_node *walker;
  walker = collisions.head;

  while (walker != NULL)
  {
    printf("Collision!!  a = %d   b = %d\n", walker->a, walker->b);
    walker = walker->next;
  }
  return;
} /* END print_collisions() */


/* -----------------------------------------------------------------------------
 * Routine:     print_coordinates
 * Description: Prints out the position coordinates of every body in the
 *              simulation.
 * Arguments:   None.
 * Returns:     Nothing.
 * -------------------------------------------------------------------------- */
void print_coordinates(void)
{
  int i;

  for (i = 0; i < num_bodies; i++)
  {
    printf("Body %d:    x = %lf    y = %lf\n", i, position[i]->x,
        position[i]->y);
  }
  printf("\n");
  return;
} /* END print_coordinates() */


/* -----------------------------------------------------------------------------
 * Routine:     error
 * Description: Prints the passed message to stderr, closes any open files, and
 *              exits the program with status of EXIT_FAILURE.
 * Arguments:   *err_msg - Pointer to the message to print.
 * Returns:     Nothing, but upon calling exits the program.
 * -------------------------------------------------------------------------- */
void error(char *err_msg)
{
  if (file != NULL)
  {
    fclose(file);
  }
  fprintf(stderr, "\n%s\n", err_msg);
  exit(EXIT_FAILURE);
} /* END error() */


/* -----------------------------------------------------------------------------
 * Routine:     routine
 * Description: description
 * Arguments:   args
 * Returns:     retval
 * -------------------------------------------------------------------------- */

/* END sequential.h */

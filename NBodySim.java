package application;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;
import javafx.util.Duration;

public class NBodySim extends Application {

	private int numBodies;
	private int radius;
	private int timesteps;

	FileReader input = null;
	Scanner scan = null;

	public static void main(String args[]) {
		launch();
	}

	@Override
	public void start(Stage stage) throws Exception {

		double xinit, yinit;

		fileInit();

		Pane canvas = new Pane();
		Scene scene = new Scene(canvas, 1800, 1000, Color.ALICEBLUE);

		Circle[] balls = new Circle[numBodies];

		for (int i = 0; i < numBodies; i++) {
			
			balls[i] = new Circle(radius, Color.BLACK);
			xinit = scan.nextDouble();
			yinit = scan.nextDouble();
			balls[i].relocate(xinit, yinit);
			canvas.getChildren().add(balls[i]);
		}

		stage.setTitle("NBODY");
		stage.setScene(scene);
		stage.show();

		Timeline timeline = new Timeline(new KeyFrame(Duration.millis(20), new EventHandler<ActionEvent>() {

			double x;
			double y;

			@Override
			public void handle(ActionEvent t) {

				for (int i = 0; i < numBodies; i++) {
					
					x = scan.nextDouble();
					y = scan.nextDouble();

					balls[i].setLayoutX(x);
					balls[i].setLayoutY(y);
				}
			}
		}));
		
		timeline.setCycleCount(timesteps - 1);
		timeline.play();
	}

	private void fileInit() {
		try {

			input = new FileReader("gui_input.txt");
			scan = new Scanner(input);

			numBodies = scan.nextInt();
			radius = scan.nextInt();
			timesteps = scan.nextInt();

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
}

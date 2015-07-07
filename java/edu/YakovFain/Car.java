public class Car {
  int distance = 0;

  public void start() {
    System.out.println("Start drive");
  }

  public void stop() {
    System.out.println("Stop drive");
  }

  public int drive(int howlong) {
    distance = howlong * 60;
    System.out.println("Driving distance: " + distance);
    return distance;
  }
}

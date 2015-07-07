public class JamesBondCar extends Car {
  public int drive(int howlong) {
    distance = howlong * 180;
    System.out.println("Driving distance: " + distance);
    return distance;
  }
}

public class App {
    public static void main(String[] args) {
        StdOut.println("ingrese el nombre del equipo1: ");
        String equipo = StdIn.readString();
        StdOut.println("ingrese el nombre del equipo2: ");
        String equipo2 = StdIn.readString();
        StdOut.print("cuantas cestas realizo el equipo " + equipo + ": ");
        int points1 = StdIn.readInt();
        StdOut.print("cuantas cestas realizo el equipo " + equipo2 + ": ");
        int points2 = StdIn.readInt();

        if (points1 > points2) {
            StdOut.println("el equipo ganador fue el equipo de " + equipo);
            StdOut.println("el equipo perdedor fue el equipo de " + equipo2);
            StdOut.println("la diferencia de puntos fue de: " + (points1 - points2));
        } else {
            StdOut.println("el equipo ganador fue el equipo de " + equipo2);
            StdOut.println("el equipo perdedor fue el equipo de " + equipo);
            StdOut.println("la diferencia de puntos fue de: " + (points2 - points1));
        }

    }
}

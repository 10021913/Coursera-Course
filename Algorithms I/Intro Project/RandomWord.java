import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String champion = "";
        String word = "";
        // Use for loop to get index
        for (int i = 1; !StdIn.isEmpty(); i++) {
            word = StdIn.readString();
            if (StdRandom.bernoulli(1.0 / i)) {
                champion = word;
            }
        }
        // Use last word if champion not set
        if (champion.isEmpty()) {
            champion = word;
        }
        // Print out champion
        StdOut.println(champion);
    }
}
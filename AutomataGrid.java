import java.io.File;
import java.io.PrintStream;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

public class AutomataGrid {
    private Set<Point2D> blackSquares;
    private Set<Point5D> blackRules;
    private int halfWidth;
    private int height;

    public static void main(String[] args) throws Exception {
        AutomataGrid ag = new AutomataGrid(
            // randomInitialRow(100), (long) (Integer.parseInt("0010000000000000000000000000000", 2))
            randomInitialRow(100), 8
        );
        ag.propagate(100);
        PrintStream ps = new PrintStream(
            new File("C:\\Users\\dang8\\github_repos\\infinite-grid\\automata_grid_output.txt")
        );
        ps.print(ag);
    }

    // give rules that result in a black square below
    public AutomataGrid(Collection<Integer> initialRow, long ruleNumber) {
        blackSquares = new HashSet<>();
        blackRules = new HashSet<>();
        for (Point5D rule : ruleSet(ruleNumber)) {
            blackRules.add(rule);
        }
        for (int i : initialRow) {
            halfWidth = Math.max(halfWidth, Math.abs(i));
            blackSquares.add(new Point2D(i, 0));
        }
    }

    public int getCell(Point2D cell) {
        if (blackSquares.contains(cell)) {
            return 1;
        }
        return 0;
    }

    public int getCell(int x, int y) {
        return getCell(new Point2D(x, y));
    }

    private void constructCell(Point2D cell) {
        Point5D neighbors = new Point5D(
            getCell(cell.getX() - 2, cell.getY() - 1),
            getCell(cell.getX() - 1, cell.getY() - 1),
            getCell(cell.getX(), cell.getY() - 1),
            getCell(cell.getX() + 1, cell.getY() - 1),
            getCell(cell.getX() + 2, cell.getY() - 1)
        );
        if (blackRules.contains(neighbors)) {
            blackSquares.add(cell);
            halfWidth = Math.max(halfWidth, Math.abs(cell.getX()));
        }
    }

    private void constructCell(int x, int y) {
        constructCell(new Point2D(x, y));
    }

    public void propagate(int steps) {
        height = steps + 3;
        for (int t = 1; t <= steps; t++) {
            for (int w = -(halfWidth + 5); w <= halfWidth + 5; w++) {
                constructCell(w, t);
            }
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int h = 0; h < height + 3; h++) {
            for (int w = -(halfWidth + 5); w <= halfWidth + 5; w++) {
                    int r = getCell(w, h);
                    if (r == 0) {
                        sb.append(" ");
                    } else {
                        sb.append("#");
                    }
                }
            sb.append("\n");
        }
        return sb.toString();
    }

    private static Point5D binaryPoint(int n) {
        String binaryString = Integer.toBinaryString(n);
        int[] binary = new int[5];
        int b = 4;
        for (int i = binaryString.length() - 1; i >= 0; i--) {
            binary[b] = Character.getNumericValue(binaryString.charAt(i));
            b--;
        }
        return new Point5D(binary[0], binary[1], binary[2], binary[3], binary[4]);
    }

    private static Collection<Point5D> ruleSet(long n) {
        Set<Point5D> rules = new HashSet<>();
        String binaryString = Long.toBinaryString(n);
        int[] binary = new int[32];
        int b = 31;
        for (int i = binaryString.length() - 1; i >= 0; i--) {
            binary[b] = Character.getNumericValue(binaryString.charAt(i));
            b--;
        }
        for (int i = 0; i < binary.length; i++) {
            if (binary[i] == 1) {
                rules.add(binaryPoint(i));
            }
        }
        return rules;
    }

    private static Collection<Integer> randomInitialRow(int halfWidth) {
        Set<Integer> ints = new HashSet<>();
        Random r = new Random();
        for (int h = -halfWidth; h <= halfWidth; h++) {
            if (r.nextInt(2) == 1) {
                ints.add(h);
            }
        }
        return ints;
    }
}
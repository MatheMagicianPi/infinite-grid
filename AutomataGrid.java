import java.io.File;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class AutomataGrid {
    private Set<Point2D> blackSquares;
    private Set<Point5D> blackRules;
    private int halfWidth;
    private int height;

    // give rules that result in a black square below
    public AutomataGrid(Collection<Integer> initialRow,
                        Collection<Point5D> statesForNextBlack) {
        blackSquares = new HashSet<>();
        blackRules = new HashSet<>();
        for (Point5D rule : statesForNextBlack) {
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
                        sb.append("[ ]");
                    } else {
                        sb.append("[=]");
                    }
                }
            sb.append("\n");
        }
        return sb.toString();
    }

    public static void main(String[] args) throws Exception {
        AutomataGrid ag = new AutomataGrid(
            List.of(0, 1, 3, 5, 6, 7, 10, 12),
            List.of(
                new Point5D(1, 1, 0, 0, 0),
                new Point5D(0, 1, 1, 0, 0),
                new Point5D(0, 1, 0, 1, 0),
                new Point5D(1, 1, 0, 1, 0),
                new Point5D(0, 1, 1, 0, 1),
                new Point5D(0, 0, 0, 1, 0),
                new Point5D(0, 0, 0, 1, 1),
                new Point5D(0, 0, 1, 0, 1),
                new Point5D(0, 0, 1, 1, 0),
                new Point5D(1, 1, 1, 1, 0),
                new Point5D(1, 1, 1, 0, 1),
                new Point5D(1, 0, 1, 1, 0)
        ));
        ag.propagate(10);
        PrintStream ps = new PrintStream(
            new File("C:\\Users\\dang8\\github_repos\\infinite-grid\\automata_grid_output.txt")
        );
        ps.print(ag);
    }
}
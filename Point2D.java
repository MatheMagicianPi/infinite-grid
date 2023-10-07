import java.util.Objects;

public class Point2D {
    private int x;
    private int y;

    public Point2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int hashCode() {
        return Objects.hash(x, y);
    }

    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (other == null || getClass() != other.getClass()) {
            return false;
        }
        Point2D otherPoint = (Point2D) other;
        if (
            x != otherPoint.x ||
            y != otherPoint.y
        ) {
            return false;
        }
        return true;
    }
}

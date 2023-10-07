import java.util.Objects;

public class Point5D {
    private int x;
    private int y;
    private int z;
    private int u;
    private int v;

    public Point5D(int x, int y, int z, int u, int v) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.u = u;
        this.v = v;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("(").append(x).append(", ")
                        .append(y).append(", ")
                        .append(z).append(", ")
                        .append(u).append(", ")
                        .append(v)
            .append(")");
        return sb.toString();
    }

    public int hashCode() {
        return Objects.hash(x, y, z, u, v);
    }

    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (other == null || getClass() != other.getClass()) {
            return false;
        }
        Point5D otherPoint = (Point5D) other;
        if (
            x != otherPoint.x ||
            y != otherPoint.y ||
            z != otherPoint.z ||
            u != otherPoint.u ||
            v != otherPoint.v
        ) {
            return false;
        }
        return true;
    }
}

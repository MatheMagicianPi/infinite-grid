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
        return true;
    }
}

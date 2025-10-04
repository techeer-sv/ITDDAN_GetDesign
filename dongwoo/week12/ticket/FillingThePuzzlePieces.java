package dongwoo.week12.ticket;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class FillingThePuzzlePieces {

    //상하좌우
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    public int solution(int[][] gameBoard, int[][] table) {
        int answer = 0;
        int len = table.length;
        //빈 공간 찾기(0)
        List<Shape> emptyShapes = findShapes(gameBoard, 0, len);
        //퍼즐 조각 찾기(1)
        List<Shape> puzzleShapes = findShapes(table, 1, len);
        // 퍼즐을 회전해가며 매칭
        boolean[] visited = new boolean[puzzleShapes.size()];
        for (Shape emptyShape : emptyShapes) {
            for (int j = 0; j < puzzleShapes.size(); j++) {
                if (visited[j]) {
                    continue;
                }
                Shape ps = puzzleShapes.get(j);
                if (ps.size() != emptyShape.size()) {
                    continue;
                }

                boolean isMatched = false;
                for (int i = 0; i < 4; i++) {
                    if (emptyShape.isEqual(ps)) {
                        answer += ps.size();
                        visited[j] = true;
                        isMatched = true;
                        break;
                    }
                    ps = ps.rotate();
                }
                if (isMatched) {
                    break;
                }
            }
        }

        return answer;
    }

    private List<Shape> findShapes(int[][] board, int target, int len) {
        List<Shape> shapes = new ArrayList<>();
        boolean[][] visited = new boolean[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (target == board[i][j] && !visited[i][j]) {
                    Shape shape = extractShape(board, new Point(j, i), target, len, visited);
                    shapes.add(shape);
                }
            }
        }
        return shapes;
    }

    private Shape extractShape(int[][] board, Point first, int target, int len, boolean[][] visited) {
        Shape shape = new Shape();
        Queue<Point> que = new LinkedList<>();

        que.add(first);
        shape.add(first);
        visited[first.y][first.x] = true;
        //상하좌우 target BFS
        while (!que.isEmpty()) {
            Point cur = que.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (ny >= 0 && ny < len
                        && nx >= 0 && nx < len
                        && board[ny][nx] == target
                        && !visited[ny][nx]) {
                    Point p = new Point(nx, ny);
                    que.add(p);
                    shape.add(p);
                    visited[ny][nx] = true;
                }
            }
        }
        shape.normalize();
        return shape;
    }

    private static class Point {
        private int x;
        private int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Shape {
        private final List<Point> points;

        public Shape() {
            this.points = new ArrayList<>();
        }

        public void add(Point p) {
            this.points.add(p);
        }

        public int size() {
            return this.points.size();
        }

        public void sort() {
            this.points.sort((t1, t2) -> {
                if (t1.x == t2.x) {
                    return Integer.compare(t1.y, t2.y);
                }
                return Integer.compare(t1.x, t2.x);
            });
        }

        public void normalize() {
            int minX = Integer.MAX_VALUE;
            int minY = Integer.MAX_VALUE;

            for (Point p : this.points) {
                minX = Math.min(minX, p.x);
                minY = Math.min(minY, p.y);
            }

            for (Point p : this.points) {
                p.x -= minX;
                p.y -= minY;
            }
            this.sort();
        }

        public boolean isEqual(Shape s) {
            for (int i = 0; i < this.size(); i++) {
                Point tp = this.points.get(i);
                Point sp = s.points.get(i);
                if (tp.x != sp.x || tp.y != sp.y) {
                    return false;
                }
            }
            return true;
        }

        public Shape rotate() {
            int maxX = 0;
            for (Point p : this.points) {
                maxX = Math.max(p.x, maxX);
            }
            Shape rotatedShape = new Shape();
            for (Point p : this.points) {
                rotatedShape.add(new Point(p.y, maxX - p.x));
            }
            rotatedShape.normalize();
            return rotatedShape;
        }
    }
}

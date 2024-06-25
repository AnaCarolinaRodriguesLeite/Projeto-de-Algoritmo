import java.util.*;

public class Main {
  static final int INF = Integer.MAX_VALUE;

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int m = scanner.nextInt();

    // Criação da lista de adjacência
    List<List<Edge>> adjList = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      adjList.add(new ArrayList<>());
    }

    for (int i = 0; i < m; i++) {
      int a = scanner.nextInt() - 1;
      int b = scanner.nextInt() - 1;
      int w = scanner.nextInt();
      adjList.get(a).add(new Edge(b, w));
      adjList.get(b).add(new Edge(a, w));
    }

    // Vetor de distâncias e vetor de visitados
    int[] dist = new int[n];
    boolean[] visited = new boolean[n];
    Arrays.fill(dist, INF);

    // Fila de prioridade (heap) para manter o próximo vértice a ser visitado
    PriorityQueue<Node> pq = new PriorityQueue<>();
    pq.add(new Node(0, 0)); // (distância, vértice)

    // Começando a busca
    dist[0] = 0;
    while (!pq.isEmpty()) {
      Node node = pq.poll();
      int currDist = node.dist;
      int currVert = node.vert;

      if (visited[currVert]) {
        continue;
      }

      visited[currVert] = true;
      if (currVert == n - 1) {
        break;
      }

      for (Edge edge : adjList.get(currVert)) {
        int neighbor = edge.to;
        int weight = edge.weight;

        if (!visited[neighbor] && dist[neighbor] > currDist + weight) {
          dist[neighbor] = currDist + weight;
          pq.add(new Node(dist[neighbor], neighbor));
        }
      }
    }

    // Verificação se há caminho para o vértice n
    if (visited[n - 1]) {
      List<Integer> path = new ArrayList<>();
      int currVert = n - 1;
      while (currVert != 0) {
        path.add(currVert + 1);

        for (Edge edge : adjList.get(currVert)) {
          int neighbor = edge.to;
          int weight = edge.weight;

          if (dist[currVert] == dist[neighbor] + weight) {
            currVert = neighbor;
            break;
          }
        }
      }
      path.add(1);
      Collections.reverse(path);
      System.out.println(path.toString().replaceAll("[\\[\\],]", ""));
    } else {
      System.out.println(-1);
    }
  }

  static class Edge {
    int to, weight;

    public Edge(int to, int weight) {
      this.to = to;
      this.weight = weight;
    }
  }

  static class Node implements Comparable<Node> {
    int dist, vert;

    public Node(int dist, int vert) {
      this.dist = dist;
      this.vert = vert;
    }

    @Override
    public int compareTo(Node other) {
      return Integer.compare(this.dist, other.dist);
    }
  }
}

class Solution {
    public Node cloneGraph(Node node) {

        if (node == null) {
            return null;
        }

        HashMap<Node, Node> map = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();

        // Clone the first node
        map.put(node, new Node(node.val));
        queue.add(node);

        while (!queue.isEmpty()) {

            Node curr = queue.poll();

            for (Node neighbor : curr.neighbors) {

                // If neighbor is not cloned
                if (!map.containsKey(neighbor)) {
                    map.put(neighbor, new Node(neighbor.val));
                    queue.add(neighbor);
                }

                // Connect cloned nodes
                map.get(curr).neighbors.add(map.get(neighbor));
            }
        }

        return map.get(node);
    }
}

function connect(root: Node | null): Node | null {
  const queue: Node[] = [root!];

  while (queue && queue[0]) {
    const currentLevel: number = queue.length;

    for (let level: number = 0; level < currentLevel; level++) {
      let currentNode: Node = queue.shift()!;

      if (level < currentLevel - 1)
        currentNode.next = queue[0];

      if (currentNode.left) 
        queue.push(currentNode.left);

      if (currentNode.right) 
        queue.push(currentNode.right);
    }
  }

  return root;
}

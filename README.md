**Python Data Structures**

In Python, data structures are like containers that help you organize and manage different types of data. Let's explore some of the basic ones with simple examples using numbers and fruits.

1. **Lists**:
   - Lists are like shopping bags where you can put multiple items.
   - Example:
     ```python
     numbers = [1, 2, 3, 4, 5]
     fruits = ['apple', 'banana', 'orange']
     ```

2. **Tuples**:
   - Tuples are similar to lists but cannot be changed once created.
   - Example:
     ```python
     dimensions = (10, 20, 30)
     colors = ('red', 'green', 'blue')
     ```

3. **Sets**:
   - Sets are like unique collections of items. They don't allow duplicates.
   - Example:
     ```python
     unique_numbers = {1, 2, 3, 4, 5}
     unique_fruits = {'apple', 'banana', 'orange'}
     ```

4. **Dictionaries**:
   - Dictionaries are like phone books where you look up a name (key) to find a number (value).
   - Example:
     ```python
     fruit_prices = {'apple': 1.99, 'banana': 0.99, 'orange': 1.49}
     ```

5. **Stacks**:
   - Stacks are like a stack of plates. You add items on top and remove from the top.
   - Example:
     ```python
     stack = []
     stack.append(1)
     stack.append(2)
     stack.pop()  # Removes 2
     ```

6. **Queues**:
   - Queues are like lines at a movie theater. First person in, first person out.
   - Example:
     ```python
     from collections import deque
     queue = deque()
     queue.append('apple')
     queue.append('banana')
     queue.popleft()  # Removes 'apple'
     ```

7. **Heaps**:
   - Heaps are like priority queues where the item with the highest (or lowest) priority comes out first.
   - Example:
     ```python
     import heapq
     heap = [5, 3, 7, 1]
     heapq.heapify(heap)  # Turns list into a heap
     heapq.heappop(heap)  # Removes and returns the smallest item
     ```

*** To run the Python script provided in the README, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where your Python script is located using the `cd` command. For example, if your script is in a directory called `Built-In-D.S` on your desktop, you would use:
   ```
   cd Desktop/Built-In-D.S
   ```

3. Once you are in the correct directory, you can run the Python script using the `python` command followed by the name of your script file. If your script is named `data_structure.py`, you would run:
   ```
   python data_structure.py
   ```

4. Press Enter to execute the command, and the script will run. You should see the output printed to the terminal.

That's it! You have successfully run your Python script from the command line.

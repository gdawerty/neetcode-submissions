class DynamicArray {
    private int[] arr;
    private int size;
    private int capacity;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.arr = new int[capacity];
        this.size = 0;
    }

    public int get(int i) {
        if (i < 0 || i >= size) throw new IndexOutOfBoundsException();
        return arr[i];
    }

    public void set(int i, int n) {
        if (i < 0 || i >= size) throw new IndexOutOfBoundsException();
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        if (size == 0) throw new RuntimeException("Array is empty!");
        int temp = arr[size - 1];
        size--;
        return temp;
    }

    private void resize() {
        capacity *= 2;
        int[] newarr = new int[capacity];
        for (int i = 0; i < size; i++) {
            newarr[i] = arr[i];
        }
        arr = newarr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}

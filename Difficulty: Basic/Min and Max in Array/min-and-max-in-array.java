import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> getMinMax(int[] arr) {

        int max_ele = arr[0];
        int min_ele = arr[0];

        for (int i = 0; i < arr.length; i++) {

            if (arr[i] > max_ele) {
                max_ele = arr[i];
            }

            if (arr[i] < min_ele) {
                min_ele = arr[i];
            }
        }

        ArrayList<Integer> result = new ArrayList<>();

        result.add(min_ele);
        result.add(max_ele);

        return result;
    }
}
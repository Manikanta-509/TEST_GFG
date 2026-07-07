<h2><a href="https://www.geeksforgeeks.org/problems/sort-first-half-in-ascending-and-second-half-in-descending1714/1">Half Ascending and Half Descending Sort</a></h2><h3>Difficulty Level : Difficulty: Basic</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an array <strong>arr </strong>of even size, sort the first half of the array in ascending order and the second half in descending order.<br></span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [10, 20, 30, 40]
<strong>Output:</strong> [10, 20, 40, 30]<br><strong>Explanation: <br></strong></span><span style="font-size: 18px;">The array is divided into two equal halves: [10, 20] and [30, 40].
The first half is already in ascending order, so it remains [10, 20].
The second half is sorted in descending order, changing [30, 40] to [40, 30].
Thus, the final array becomes [10, 20, 40, 30].<br></span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">arr[] = [5, 4, 6, 2, 3, 8, 9, 7]
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> [2, 4, 5, 6, 9, 8, 7, 3] 
</span><span style="font-size: 18px;"><strong>Explanation: <br></strong>The array is divided into two equal halves: [5, 4, 6, 2] and [3, 8, 9, 7].
Sorting the first half in ascending order gives [2, 4, 5, 6].
Sorting the second half in descending order gives [9, 8, 7, 3].
Combining both halves, the final array becomes [2, 4, 5, 6, 9, 8, 7, 3].</span>
</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:&nbsp;</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>6</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;
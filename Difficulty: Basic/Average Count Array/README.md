<h2><a href="https://www.geeksforgeeks.org/problems/average-count-array2215/1">Average Count Array</a></h2><h3>Difficulty Level : Difficulty: Basic</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an integer array <strong>arr[]</strong> and an integer <strong>x</strong>.</span></p>
<p><span style="font-size: 18px;">For each index i (0-based), calculate the floor value of the average of arr[i] and x:&nbsp; </span><strong><span style="font-size: 18px;">avg = floor((arr[i] + x) / 2)</span></strong></p>
<p><span style="font-size: 18px;">Then, count how many times this calculated value occurs in the original array arr[].</span></p>
<p><span style="font-size: 18px;">Store this count at index i of a new array <strong>result[]</strong>.</span></p>
<p><span style="font-size: 18px;">Return the array result[].</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [2, 4, 8, 6, 2], x = 2
<strong>Output:</strong> [2, 0, 0, 1, 2]
<strong>Explanation:</strong> </span><span style="font-size: 18px;"><span style="font-size: 18px;">For each element,
arr[0] = 2: floor((2 + 2) / 2) = 2. Value 2 appears 2 times.
arr[1] = 4: floor((4 + 2) / 2) = 3. Value 3 does not appear,.
arr[2] = 8: floor((8 + 2) / 2) = 5. Value 5 does not appear.
arr[3] = 6: floor((6 + 2) / 2) = 4. Value 4 appears once.
arr[4] = 2: floor((2 + 2) / 2) = 2. Value 2 appears 2 times.</span></span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input :</strong><span style="font-size: 18px;"> arr[] = [9, 5, 2, 4, 0, 3], x = 3 </span><strong style="font-size: 18px;">
Output :</strong><span style="font-size: 18px;"> [0, 1, 1, 1, 0, 1] <br></span><strong style="font-size: 18px;">Explanation: </strong></span><span style="font-size: 18px;">The calculated average values are: [6, 4, 2, 3, 1, 3]
Their frequencies in arr[] are: [0, 1, 1, 1, 0, 1]</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span><br><span style="font-size: 18px;">1 ≤ arr.size() ≤ 10<sup>5</sup></span><br><span style="font-size: 18px;">0 ≤ x ≤ 10<sup>5</sup></span><br><span style="font-size: 18px;">0 ≤ arr[i] ≤ 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Mathematical</code>&nbsp;<code>logical-thinking</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;
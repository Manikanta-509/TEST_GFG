<h2><a href="https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1">Allocate Minimum Pages</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span class="cf0" style="font-size: 14pt;">Given an array <strong>arr[] </strong>of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:</span></p>
<ul>
<li><span class="cf0" style="font-size: 14pt;">Each student receives atleast one book.</span></li>
<li><span class="cf0" style="font-size: 14pt;">Each student is assigned a contiguous sequence of books.</span></li>
<li><span class="cf0" style="font-size: 14pt;">No book is assigned to more than one student.</span></li>
</ul>
<p class="pf0"><span class="cf0" style="font-size: 14pt;">The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.</span></p>
<p class="pf0">&nbsp;</p>
<p class="pf0"><span class="cf0" style="font-size: 14pt;"><strong>Note:</strong> Return <strong>-1</strong> if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [12, 34, 67, 90], k = 2
<strong>Output: </strong>113
<strong>Explanation: </strong>Allocation can be done in following ways:
             =&gt; [12] and [34, 67, 90] Maximum Pages = 191
             =&gt; [12, 34] and [67, 90] Maximum Pages = 157
             =&gt; [12, 34, 67] and [90] Maximum Pages = 113.
             Therefore, the minimum of these cases is 113, which is selected as the output.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [15, 17, 20], k = 5
<strong>Output: </strong>-1
<strong>Explanation: </strong></span><span style="font-size: 14pt;">We must assign at least one book per student, but we have only 3 books, and 5 students. <span class="cf0">This is impossible, because two students would have to receive no book, which violates the constraint.</span></span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤&nbsp; arr.size() ≤ 10<sup>6</sup><br>1 ≤ arr[i], k ≤ 10<sup>3</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Infosys</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Google</code>&nbsp;<code>Codenation</code>&nbsp;<code>Uber</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Searching</code>&nbsp;<code>Divide and Conquer</code>&nbsp;<code>Algorithms</code>&nbsp;
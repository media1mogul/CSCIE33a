```
perftest@ubuntu:~/DevCode/CSCIE33a/Project_1$ git commit
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	scratch/2021_09_17-13_54-workingSession(0).md
	scratch/2021_09_17-13_54-workingSession.md

nothing added to commit but untracked files present (use "git add" to track)
```



This is where I start.
This is where I left off in the last session.
At this point
 - I have modified and committed changes to index.html via the github web interface. This means that the actual origin code is changed.
 - I have modified and commited changes locally. This  means that the local copy of origin has also been changed.

So now I will try to push my committed local changes up to the actual origin
 - I added the markdown file and committed it locally.

<pre><font color="#4E9A06"><b>erftest@ubuntu</b></font>:<font color="#3465A4"><b>~/DevCode/CSCIE33a/Project_1</b></font>$ git pull
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), 822 bytes | 137.00 KiB/s, done.
From https://github.com/media1mogul/CSCIE33a
   3015446..90c5bd3  main       -&gt; origin/main
Merge made by the &apos;recursive&apos; strategy.
 Project_1/scratch/index.html | 5 <font color="#4E9A06">+++</font><font color="#CC0000">--</font>
 1 file changed, 3 insertions(+), 2 deletions(-)
<font color="#4E9A06"><b>perftest@ubuntu</b></font>:<font color="#3465A4"><b>~/DevCode/CSCIE33a/Project_1</b></font>$ git push
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 861 bytes | 861.00 KiB/s, done.
Total 9 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/media1mogul/CSCIE33a
   90c5bd3..9117827  main -&gt; main
Everything up-to-date
</pre>

This did not do what I thought would happen.
It appears that the conflict was resolved automatically.


**Tech notes**

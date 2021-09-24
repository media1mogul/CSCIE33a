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

<pre><font color="#4E9A06"><b>perftest@ubuntu</b></font>:<font color="#3465A4"><b>~/DevCode/CSCIE33a/Project_1</b></font>$ git push
Username for &apos;https://github.com&apos;: mike@reekie.us
Password for &apos;https://mike@reekie.us@github.com&apos;: 
To https://github.com/media1mogul/CSCIE33a
 <font color="#CC0000">! [rejected]       </font> main -&gt; main (fetch first)
<font color="#CC0000">error: failed to push some refs to &apos;https://github.com/media1mogul/CSCIE33a&apos;</font>
<font color="#C4A000">hint: Updates were rejected because the remote contains work that you do</font>
<font color="#C4A000">hint: not have locally. This is usually caused by another repository pushing</font>
<font color="#C4A000">hint: to the same ref. You may want to first integrate the remote changes</font>
<font color="#C4A000">hint: (e.g., &apos;git pull ...&apos;) before pushing again.</font>
<font color="#C4A000">hint: See the &apos;Note about fast-forwards&apos; in &apos;git push --help&apos; for details.</font>
To https://github.com/media1mogul/CSCIE33a
 <font color="#CC0000">! [rejected]       </font> main -&gt; main (fetch first)
<font color="#CC0000">error: failed to push some refs to &apos;https://github.com/media1mogul/CSCIE33a&apos;</font>
<font color="#C4A000">hint: Updates were rejected because the remote contains work that you do</font>
<font color="#C4A000">hint: not have locally. This is usually caused by another repository pushing</font>
<font color="#C4A000">hint: to the same ref. You may want to first integrate the remote changes</font>
<font color="#C4A000">hint: (e.g., &apos;git pull ...&apos;) before pushing again.</font>
<font color="#C4A000">hint: See the &apos;Note about fast-forwards&apos; in &apos;git push --help&apos; for details.</font></pre>
	


**Tech notes**

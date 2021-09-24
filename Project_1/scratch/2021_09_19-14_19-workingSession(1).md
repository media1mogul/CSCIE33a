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

Try again.
 - Introduced conflicts to the same line in index.html from the web adn from local.
 - directly commited the web based changes to origin/main.
 - committed the local changes to the local origin/main.
 
 <pre><font color="#4E9A06"><b>perftest@ubuntu</b></font>:<font color="#3465A4"><b>~/DevCode/CSCIE33a</b></font>$ git push
Username for &apos;https://github.com&apos;: media1mogul
Password for &apos;https://media1mogul@github.com&apos;: 
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
<font color="#C4A000">hint: See the &apos;Note about fast-forwards&apos; in &apos;git push --help&apos; for details.</font>
</pre>
 
Ok. So I do a git pull and this time I see the conflict as I should.

<pre><font color="#4E9A06"><b>perftest@ubuntu</b></font>:<font color="#3465A4"><b>~/DevCode/CSCIE33a</b></font>$ git pull
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), 793 bytes | 793.00 KiB/s, done.
From https://github.com/media1mogul/CSCIE33a
   9117827..2866172  main       -&gt; origin/main
Auto-merging Project_1/scratch/index.html
CONFLICT (content): Merge conflict in Project_1/scratch/index.html
Automatic merge failed; fix conflicts and then commit the result.
<font color="#4E9A06"><b>perftest@ubuntu</b></font>:<font color="#3465A4"><b>~/DevCode/CSCIE33a</b></font>$ 

</pre>

I  used git -a to commit the local fixed html to the local origin/main.

```
perftest@ubuntu:~/DevCode/CSCIE33a$ git commit -a
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Project_1/scratch/2021_09_17-13_54-workingSession(0).md
	Project_1/scratch/2021_09_17-13_54-workingSession(1).md
	Project_1/scratch/2021_09_17-13_54-workingSession(2).md
	Project_1/scratch/2021_09_17-13_54-workingSession(3).md
	Project_1/scratch/index(0).html
	Project_1/scratch/index(1).html

nothing added to commit but untracked files present (use "git add" to track)
```
Now I did the git push.

```
perftest@ubuntu:~/DevCode/CSCIE33a$ git push
Username for 'https://github.com': media1mogul
Password for 'https://media1mogul@github.com': 
Enumerating objects: 26, done.
Counting objects: 100% (25/25), done.
Delta compression using up to 4 threads
Compressing objects: 100% (13/13), done.
Writing objects: 100% (16/16), 2.80 KiB | 1.40 MiB/s, done.
Total 16 (delta 9), reused 0 (delta 0)
remote: Resolving deltas: 100% (9/9), completed with 3 local objects.
To https://github.com/media1mogul/CSCIE33a
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
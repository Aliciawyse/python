#Counting Organizations

<p>
This application will read the mailbox data (mbox.txt) count up the
number email messages per organization (i.e. domain name of the email
address) using a database with the following schema to maintain the counts.
</p>

<pre>CREATE TABLE Counts (org TEXT, count INTEGER)
</pre>

When you have run the program on mbox.txt upload the resulting database file above for grading.

This code can be used as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
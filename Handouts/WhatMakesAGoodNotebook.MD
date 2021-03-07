# What makes a good notebook?

## Purpose

As I was working on homework, I've noticed varying qualities of the notebooks submitted.  Because of that, I wanted to better specify what makes a good notebook, and why you should care about it.

A good notebook is written toward the audience you're sending the notebook to.  Your audience matters a lot.  Common audiences for notebooks could be:

1.  Business Users - So they can verify specific output/logic.  These people won't be running the notebooks, but would be interested in the visuals.
2.  Developers - Notebooks can aid in explaining a process and/or problem.  If a bug is found, demonstrating the incorrect, and correct answer, can be done in a notebook.
3.  Yourself - Notebooks can be excellent playgrounds for future reference and experimentation.

There are more audiences, too.  But the point is, your audience matters in the notebook.

## General Structure

In lecture 1, I recommended that you split your notebook into multiple sections.  Those sections are:

1.  A main summary section.  What's the notebook name, what's the purpose, what was changed, what libraries does it require, what setup is required, what dependencies may exist.
2.  A setup/helper section.  Your functions, global variables of interest (e.g. file locations).
3.  A work-section.  The calling of those functions, the processing of data.

These sections aren't "hard and fast" rules, but are large buckets.  For each one, there could be sub-sections as appropriate.  For example, in the work-section, you could have sub-sections such as:

1.  File loads and data massaging
2.  Analysis of the data
3.  Graphs and final outcomes
4.  A summary, conclusion.

In short, check out near _any_ research paper.  These are derived based off a structure similar to those.

## How grades are determined

It's worth noting how I determine grades.  Every homework/test has a certain percentage (roughly 30%) that's dedicated toward the readability of your notebooks.  You could have a case where someone makes a simple mistake, but has a good notebook in terms of quality, and will place higher than someone who purely got the answer right.

The way I physically grade homework is fairly simple.  I will review every line you write in a notebook.  I create notes for different implementations/fields.  I then have a separate list that has the ordering of how students did in relation to each other.  At the end, I assign grades based off the A/B scale.

There is one time the above isn't true.  If I can tell you're not trying and provide entirely incorrect implementation or missing major steps, then that will grade significantly lower.  

Factors that determine how you're placed, in comparison to other students:

1.  The clarity of your notebooks - good names, good functions, good choices.
2.  That you got the right answer.
3.  That you're trying, moving on to another part of the problem if needed.
4.  The creativity of your solution.

So, there are more factors in place than simply getting it right.  Most everyone gets the homework right.  What will matter more is how you got to the answer, and how production-quality your notebook is.

## What I'm looking for

A good notebook is written toward the audience you're sending the notebook to.  In the case of the class, you're showing me information that's far more than "did you get the right answer".  The following will depend if you're understanding the concepts well or not, but them as a whole include, but not limited to:

* _What did you try, what worked and what didn't._  This is incredibly important if you don't get the right answer or are fuzzy with logic.  One thing I've seen is people will put a markdown cell with code they tried that didn't work - in other words showing your work.
* _Why you picked a specific strategy._ Why did you choose to do a computation in a specific way.  This relates heavily to the first option.
* _How easy is your notebook to follow._ This is a clarity point.  If I have to go through extra mental hoops to read your notebook, then this'll impact your grade.
* _That you're trying._ I can't emphasize this enough.  I want to see you trying at the homework, trying different things, and where you're struggling at.  If you end up not getting the right answer, or it's questionable if you're getting code from stack overflow and not understanding the concepts, then this is bad.  Go into this with little ego, and show pain points so we can address them.

There's a large difference between showing too much and not showing enough.  When in doubt, showing more is better.  Some strategies I've seen used by students include:

1.  Showing multiple ways of approaching the solution.  These both would work, but show they're exploring multiple ways of solving the problem.  This has a huge impact on the ranking.
2.  If they're struggling with a particular implementation, to change the cell to text or markdown, or comment out the code.  They have a part where they explain what they were trying to get at, and that they aren't understanding it.
    * In this case, I spend lots of time on the notebook, writing reasons why something didn't work, and what to try.
    

**Remember** Your goal here is to learn.  The grade, in my view, is secondary.  As long as you're trying, making an effort, and putting in time then you're going to get in the A-B range.  If you're not trying, or it's clear you don't care, you **will** get lower than that.  

# Good vs Bad Names

The lecture video goes into this a bit more detailed, but for a summary:

1.  Avoid abbreviations unless you're using abbreviations present in the domain.
    * For example: CoB may make sense to many of us, given the College of Business.  But may not for others.  So notebooks aimed toward someone outside the college should not use abbreviations.
    * Same thing goes with stuff like `cntr` vs `counter` and the like.  When in doubt, avoid the abbreviations entirely.
    
2.  Use expressive names, when possible, and avoid defining the type (going forward, given our heavy use of primitives in the past, it was okay - now going forward is not)
    * Example: `inputFile` is descriptive.  `f` is not.
    * Example: `myMatrix` is redundant (matrix listed twice), and pointless.  `randomMatrix` is better, but still somewhat redundant.  Looking in the past, `randomMatrix` should be used.  In the future, assuming this is something like weather, a better name would be `weather`
    
There's a really good book I recommend that talks about this kind of stuff heavily, along with other best practices.  

https://www.pearson.com/us/higher-education/program/Martin-Clean-Code-A-Handbook-of-Agile-Software-Craftsmanship/PGM63937.html

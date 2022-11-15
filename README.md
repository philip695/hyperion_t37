# HyperionDev Bootcamp Task 37 #

This file describes how to run the script produced for Task 37.

Assuming you are using the command line, switch to
the directory containing the project files, and run
the following commands:

> docker build -t garden_path .

> docker run --name garden garden_path

You should see output beginning:

> (I, 'I', 4690420944186131903), (told, 'told', 1245643389253732868), (the, 'the', 7425985699627899538), (man, 'man', 3104811030673030468), (the, 'the', 7425985699627899538), (horse, 'horse', 9866490340549498003), (kicked, 'kicked', 3292043087309000153), (the, 'the', 7425985699627899538), (doctor, 'doctor', 18058202148154971361), (would, 'would', 6992604926141104606), (cure, 'cure', 910830628473846539), (him, 'him', 1739263527992748485), (., '.', 12646065887601541794)]
[('I', 'PRON'), ('told', 'VERB'), ('the', 'DET'), ('man', 'NOUN'), ('the', 'DET'), ('horse', 'NOUN'), ('kicked', 'VERB'), ('the', 'DET'), ('doctor', 'NOUN'), ('would', 'AUX'), ('cure', 'VERB'), ('him', 'PRON'), ('.', 'PUNCT')]
[]

The Python script garden.py contains comments on
the entity recognition and POS tagging performed
by the script.


import spacy

# Load a model for English.
nlp = spacy.load('en_core_web_sm')

# 1. Use some Garden Path sentences or think up your own (at least 5).
# I thought these up for myself.
gardenpathSentences = [
    "I told the man the horse kicked the doctor would cure him.",
    "The rotten board boats as easily as the reputable.",
    "Because she often swims the river seems familiar to her.",
    "The household cavalry charged by the 11th hussars were destroyed.",
    "The drunk man the battlements of Elsinore.",
    "The Dutch bloom in the pursuit of art in the sixteenth century.",
    "Mr Baker said the florist sent the bouquet was ecstatic.",
    "Christmas presents difficulties for the inhabitants of Easter Island."
]

# 2. Tokenise and perform Entity recognition for each of the sentences
#    after you have stored them in a list called gardenpathSentences.
# We loop through the sentences, analysing each one using the model
# and printing out tokens, POS tags and entities.
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(token, token.orth_, token.orth) for token in doc])
    print([(token.text, token.pos_) for token in doc])

    # Using spacy.explain to provide human-readable explanations of the entity labels.
    print([(i, i.label_, i.label, spacy.explain(i.label_)) for i in doc.ents])

    # Adding a blank line for clarity.
    print()

# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities
#    you found that spaCy gave one of the words of your sentences - did you expect this?

# Entities
# The model correctly identified 'Christmas' and 'the sixteenth century' as dates,
# '11th' as an ordinal number and 'Baker' as a person (but the omission of 'Mr' from
# that entity was a bit surprising). It also correctly identified 'Easter Island' as
# a location, which I did not necessarily expect; I thought there might be the
# potential for confusion with the date 'Easter', but in hindsight I am not surprised
# the model could handle this as the collocation 'Easter Island' is distinctive. The
# surprise here was 'Elsinore', which is mistakenly identified as an organisation.
# Without knowing more about how the model identifies locations and organisations, it
# is hard to say why this was identified as an organisation when it is in fact a
# location. The label NORP 'Nationalities or religious or political groups' for
# 'Dutch' is accurate; entity recognition appears not to distinguish between
# adjectives of nationality and nouns referring collectively to nationals of a
# country. As discussed below, however, this does create an issue for POS tagging.

# POS Tags
# Given that Garden Path Sentences present particular difficulties for POS tagging,
# it seemed worth checking what the results of POS tagging on these sentences would
# be (although the task instructions do not seem to require this). In some cases,
# the broad POS tags are accurate (for example, for the first sentence). This may
# mask difficulties that the model would experience in correctly identifying the
# syntactic structure of these sentences, since the broad parts of speech are
# essentially the same whatever our interpretation of the syntactic structure.
# On the other hand, the model clearly struggles with adjectives used substantively,
# as in the second sentence (here 'rotten' is substantive; it has the sense 'rotten
# people'). Noun/verb homonymy also presents problems; again, the second sentence
# demonstrates this, as 'board' is treated as a noun by the tagger, when in fact it
# is part of the verb 'to board'. The tagger copes, however, with a similar problem
# in the final sentence, where 'presents' is correctly analysed as a verb, although
# the common collocation 'Christmas presents' (in which 'presents' is usually a
# noun) might have been expected to create problems. In the fourth sentence, the
# word 'household' is tagged as a noun rather than an adjective, which is somewhat
# surprising given that it is immediately followed by the noun 'cavalry', and
# 'household' is not an uncommon adjective. Overall, however, the tagger produces
# quite effective results despite the difficulties presented by these sentences.

mylist = ['I wish to complain about this parrot what I purchased not half an hour ago from this very boutique.', "Oh yes, the, uh, the Norwegian Blue...What's,uh...What's wrong with it?", "I'll tell you what's wrong with it, my lad. 'E's dead, that's what's wrong with it!", "No, no, 'e's uh,...he's resting."]

import pickle

with open("parrot.pkl", "wb") as f:
    pickle.dump(mylist, f)
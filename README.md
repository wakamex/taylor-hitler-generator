This is a markov chain generator that generates text based on Taylor Swift lyrics and Hitler Quotes. 

# INSTALL

`pip install -r requirements.txt`

# RUN

`python markov_chain.py`

`python similarity.py`

result of `similarity.py` as of 2023-09-27:
```
char_cutoff=51.570797086358425
num_lines_above_cutoff=1269 out of num_lines=13971 = 9.08%
compared to len(hitlers)=154
len(tokenized_lyrics)=1269
len(tokenized_hitlers)=154
--- SIMILARITY PAIR #1 ---
Taylor: Never take advice from someone who's falling apart (You should find another).
Hitler: We want a society with neither castes nor ranks and you must not allow these ideals to grow within you!
--- SIMILARITY PAIR #2 ---
Taylor: And nothin' we say is gonna save us from the fallout.
Hitler: The world has no reason for fighting in our defense, and as a matter of principle God does not make cowardly nations free...
--- SIMILARITY PAIR #3 ---
Taylor: 'Cause I'm not your princess, this ain't our fairytale.
Hitler: Either we are a sovereign state, or we are not! As long as we are not, we have no business in a community of sovereign states.
--- SIMILARITY PAIR #4 ---
Taylor: And therein lies the issue, friends don't try to trick you.
Hitler: A man does not die for something which he himself does not believe in.
--- SIMILARITY PAIR #5 ---
Taylor: This is why we can't have nice things, darling (Darling).
Hitler: The root of the whole evil lay, particularly in Schonerer's opinion, in the fact that the directing body of the Catholic Church was not in Germany, and that for this very reason alone it was hostile to the interests of our nationality.
--- SIMILARITY PAIR #6 ---
Taylor: 'Cause coming back around here would be bad for your health.
Hitler: The disastrous consequences of widespread European butchery in the future would be even worse.
6 similar pairs at threshold 0.8
```
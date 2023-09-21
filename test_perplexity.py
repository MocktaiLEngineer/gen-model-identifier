from gen_model_identifier.perplexity import rank_by_perplexity

candidate_models = [
    "gpt2",
    "distilgpt2",
    "facebook/opt-350m",
    "lvwerra/gpt2-imdb",
]

text = (
    "Brad Cooper, who plays the lead character, is a very good actor. He is a very good"
)

model2perplexity = rank_by_perplexity(text, candidate_models)

print(model2perplexity)
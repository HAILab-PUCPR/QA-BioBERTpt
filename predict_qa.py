#!/usr/bin/env python
# coding: utf-8


import transformers
from transformers import pipeline

def predict(pergunta, contexto):
        
    print('entrou na predict')
    print('pergunta:', pergunta)
    print('contexto:', contexto)

    model_name = 'pucpr/bioBERTpt-squad-v1.1-portuguese'
    nlp = pipeline("question-answering", model=model_name)

    result = nlp(question=pergunta, context=contexto)

    return result
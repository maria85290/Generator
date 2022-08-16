
'''
Implementeção do modelo T5 para sumarization
'''

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch



def T5_summarization_model (text):
    # initialize the model architecture and weights
    t5model = T5ForConditionalGeneration.from_pretrained("t5-base")
    # initialize the model tokenizer
    t5tokenizer = T5Tokenizer.from_pretrained("t5-base")
    device = torch.device('cpu')
    
    t5tokenized_text = t5tokenizer.encode("summarize:"+ text,
                                    truncation=True,
                                    return_attention_mask=True,
                                    add_special_tokens=True, 
                                    padding='max_length',     
                                    return_tensors="pt").to(device)


    t5summary_ids =  t5model.generate(input_ids=t5tokenized_text,
                    num_beams=3,  ##modelo olha para 3 possiveis palavras
                    min_length=20, ## number min of tokens
                    max_length=70,  ##number maximo of tokens
                    repetition_penalty=1.0,
                    early_stopping=True)

    output = t5tokenizer.decode(t5summary_ids[0],  
                             skip_special_tokens=True, 
                             clean_up_tokenization_spaces=True)
    return  output


def main(text):
  T5_summarization_model(text)
  
  
if __name__ == '__main__':
    main()
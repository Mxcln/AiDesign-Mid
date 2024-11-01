import os
import sys

import torch
from torch.utils.data import Dataset
from torch.utils.data.dataloader import DataLoader

from mingpt.model import GPT
from mingpt.trainer import Trainer
from mingpt.utils import set_seed, setup_logging, CfgNode as CN
from train import get_config
from train import CharDataset

# -----------------------------------------------------------------------------

if __name__ == '__main__':

    # you can specify the contexts here. each context will be used to generate a completion
    contexts=["康德认为","黑格尔","美学的意义在于","如果把哲学","在这儿个问题中","辩证地","思维律","知性","伦理","先验的","上帝"]

    # get default config and overrides from the command line, if any
    config = get_config()
    config.merge_from_args(sys.argv[1:])
    print(config)
    setup_logging(config)
    set_seed(config.system.seed)

    # construct the training dataset
    text = open('input.txt', 'r', encoding='utf-8').read() # don't worry we won't run out of file handles
    # print(text)
    train_dataset = CharDataset(config.data, text)
    # construct the trainer object
   
    # construct the model
    config.model.vocab_size = train_dataset.get_vocab_size()
    config.model.block_size = train_dataset.get_block_size()
    model = GPT(config.model)
    trainer = Trainer(config.trainer, model, train_dataset)
    model.load_state_dict(torch.load('./output/model.pt'))
    model.eval()
    # sample from the model...
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    for index, context in enumerate(contexts):
        x = torch.tensor([train_dataset.stoi[s] for s in context], dtype=torch.long)[None,...].to(trainer.device)
        y = model.generate(x, 200, temperature=1.0, do_sample=True, top_k=10)[0]
        completion = ''.join([train_dataset.itos[int(i)] for i in y])
        print(f"{index + 1}: {completion}\n")

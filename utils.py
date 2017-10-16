from model import *

def load_tag_to_idx(filename):
    print("loading tag_to_idx...")
    tag_to_idx = {}
    fo = open(filename)
    for line in fo:
        line = line.strip()
        tag_to_idx[line] = len(tag_to_idx)
    fo.close()
    return tag_to_idx

def save_tag_to_idx(filename, tag_to_idx):
    print("saving tag_to_idx...")
    word_to_idx = {}
    fo = open(filename, "w")
    for tag, _ in sorted(tag_to_idx.items(), key = lambda x: x[1]):
        fo.write("%s\n" % tag)
    fo.close()
    return

def load_word_to_idx(filename):
    print("loading word_to_idx...")
    word_to_idx = {}
    fo = open(filename)
    for line in fo:
        line = line.strip()
        word_to_idx[line] = len(word_to_idx)
    fo.close()
    return word_to_idx

def save_word_to_idx(filename, data):
    print("saving word_to_idx...")
    word_to_idx = {}
    fo = open(filename, "w")
    for sent, tags in data:
        for word in sent:
            if word not in word_to_idx:
                word_to_idx[word] = len(word_to_idx)
                fo.write("%s\n" % word)
    fo.close()
    return word_to_idx

def sent_to_idx(sent, word_to_idx):
    idxs = [word_to_idx[w] for w in sent]
    return Var(LongTensor(idxs))

def load_checkpoint(filename, model):
    print("loading model...")
    checkpoint = torch.load(filename)
    epoch = checkpoint["epoch"]
    model.load_state_dict(checkpoint["state_dict"])
    print("saved epoch = %d" % checkpoint["epoch"])
    return epoch

def save_checkpoint(filename, epoch, model):
    print("saving model...")
    checkpoint = {}
    checkpoint["epoch"] = epoch
    checkpoint["state_dict"] = model.state_dict()
    torch.save(checkpoint, filename + ".epoch%d" % epoch)

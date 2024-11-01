# AiDesign-Mid

This is the repository for the Midterm project of the course AI Design 2H2024.

## Team members
- [Yang Yuanda/杨远达](21307140079@m.fudan.edu.cn); Student ID: 21307140079
- [Li Xinran/李欣然](21307140025@m.fudan.edu.cn); Student ID: 21307140025

## Requirements

Train a language model. Choose your own dataset, model architecture, and training method; there are no restrictions on the size, languages.

Requirements: the model must be able to run successfully and generate 10 different coherent and unambiguous sentences. 

## Project Description

### 1. Project Structure

- `minGPT/`: 3rd party code for the MinGPT model. We use MinGPT as our model architecture.
- `philosiphy_gpt/`: Our code for training the language model, which focuses on the philosophy dataset.
    - `output/`: The output directory for the trained model and test result.
    - `input.txt`: The dataset we use for training the language model.
    - `train.py`: The training python script.
    - `test.py`: The testing python script.


### 2. MinGPT

We choose to use MinGPT as our model architecture. MinGPT is a PyTorch reimplementation of the GPT model. It is a simple, efficient, and effective version of GPT. We choose MinGPT because it is easy to use and has a good performance.

The core code of MinGPT is in the `minGPT/mingpt` directory:
- `model.py`: The model architecture of MinGPT.
- `trainer.py`: The training script of MinGPT.
- ...

### 3. Dataset

We choose the philosophy dataset as our training dataset(cause we have a interesting philosophy course this semester lol). The dataset is in the `philosiphy_gpt/input.txt` file. The dataset is a collection of philosophy books from the Internet, including:

* 《哲学问题》，伯特兰·罗素
* 《幸福之路》，伯特兰·罗素 
* 《西方哲学史》，伯特兰·罗素
* 《存在与时间》，马丁·海德格尔
* 《第一哲学沉思》，勒内·笛卡尔

We made some simple preprocessing on the dataset, including removing the title of the book and the author's name; removing the line breaks; restructured the text to keep them synchronized. The dataset is about 3.25MB in size, with 1144348 characters, and 3570 of them are unique.

### 4. Training

We train the language model on the philosophy dataset using MinGPT. Considering the limited CPU/GPU resources, we choose to use **gpt2** model architecture with 12 layers, 12 heads, and 768 hidden size, which could contains 124M parameters. Some of the hyperparameters are as follows:

- `n_layer`: 12
- `n_head`: 12
- `n_embd`: 768
- `batch_size`: 64
- `learning_rate`: 3e-4
- `betas`: (0.9, 0.95)

Then, you can train the model using the following command:
```bash
python train.py --trainer.max_iters=20000
```
Also, if you already have a trained model in `philosiphy_gpt/output/`, running the script above will continue training the model from the last checkpoint.

We train the model for 20000 iterations, and the training process takes about 3 hours on a single NVIDIA A10 GPU with 24G memory. In the End, the model reaches the loss around 0.20. You can see the sample output and loss rate as follows:

![loss](pic/sample.jpg)
 
The trained model is saved in the `philosiphy_gpt/output/` directory.

### 5. Testing

We use `test.py` to test the trained model. You can run the following command to test the model:
```bash
python test.py > ./output/result.txt
```
Also, you can change the prompt in the `test.py` file to test the model with different prompts.

```python
# you can specify the contexts here. each context will be used to generate a completion
contexts=["康德认为","黑格尔","美学的意义在于","如果把哲学","在这儿个问题中","辩证地","思维律","知性","伦理","先验的","上帝"]
```

The testing process is simple: we input a prompt word/sentence to the model, and the model will generate the next 200 characters based on the prompt. We test the model with 10 different prompts, and the model generates 10 different coherent and unambiguous sentences. You can see the test result in the `philosiphy_gpt/output/result.txt` file. Here are some examples:

```markdown

1: **康德**认为它是一个慈善哲学家，但是当他在形而上学方面做出了重大感情的作用时，那就是他原始终不快地提出来。
不过，问题的根子在于，无论如何我们从它所作的为什么地方开始，这个预示出必然的结果，预示着我们的预言，预料在有关者个人的心理中是集体的，我们的个人就少得多了。因此，，某些人的快乐放在我们心灵魂方面的东西，这种东西几乎有不恰当地被我们所认识，因为在我们说心灵与心灵之前一切心灵都是共相的，并且它包括我们并不因

2: **黑格尔**不同的看法容易驳倒。他说，实体的本质上显然是并不相同的，因此在的存在倒是一种。
但是，此在的一切行为都从它本身那里扯开，不向先行进入这一可能性中。在先行着的决心那里被经验到的。如果时间性是在这里源始地昭示出来，那么可以推测先行的决心的时间性是时间性本身的一种特具一格的样式。时间性可以在种种不同的可能性中以种种不同的方式到〔其〕时〔机〕。此在的本真状态与非本真状态这两种基本的生存可能性在存在论上根据

3: **美学的意义在于**希腊化的时代的一切知识，就都是根据他表述时间的理论，“意义是其自身的”或“性质”。可是我们必须把所有的希腊人都看成是人”这一陈述分为种矛盾，所以他就认为唯有有智慧的人的灵魂才是如此。他的兴趣并不象晚期的斯多葛派那样彻底是伦理的；事实上他把逻辑弄成了根本的东西。假言三段论和选言三段论以及“选言”这个名词，都出自斯多葛派，对文法的研究和对名词的意义的各种“格”变化的创见，也都出自斯多葛派。克吕西普，或

4: **如果把哲学**思考的表达，那么也就必须研究它们的真理。
还有一个重要之点，在这一点上经验主义者之反对理性主义者也是正确的。除了依靠经验的帮助而外，我们无法知道有什么东西是存在的这个意义问题的真理并不属于我们。
然而，现在我们就可以明了，区别真理的判断和虚妄的判断究竟是什么了。为了这个目的，我们将要采用某些定义。在每一项判断行为中，都有一个执行判断的心灵，还有涉及到它所判断的几造。我们把心灵称作判断中的主体，其余

5: **在这儿个问题中**，首先可以发现为如此尖锐，以至于这种对象的虚妄的意义，竟然后再没有什么东西是可以再进一步加以领会的，而是一种衍生样式的完结构，没有一种根本假的判断。
应当记忆，这个判断（它和它们所涉及的判断一样，并不是记忆的组成部分，但是它和它的性质完成成分有联系。比如说，如说，它是一堆事（结果），只要我们不是一个它的表象（只要想象确切实的联系，便不是心灵的一个观念；因此，像印象出现在我们彼此之间的联合，并且这种

6: **辩证地**被感知到”，那是一种被感知所感知的东西，而是属于心的；况且，距离不是凭看感知的，而是经验的结果，是判断出来的；一个生来瞎眼、但现在初次能看东西的人，视觉对象对于他就不会显得有距离。
在第二篇对话的开头，海拉司极力主张脑子里的某些痕迹为感觉作用的起因，但是费罗诺斯回驳他说：“脑子既然是可感物，只存在于心中。”
这本对话的其余部分不那么有意思，没必要再讲了。现在我们给贝克莱的主张作一个分析批判。贝克莱

7: **思维律**，而且还拿它当假定你有这样极端；然而，如果说地球自转，旋转假说用尽法和太阳不转，地球自己便每天空回转一周的一个钟内，沿着水平方向运动的加速度，这种素材表现为物体的运动性定律。他叙述了第一运动定律，然后立即应用于心理学：想像是衰退中的感觉，两者都是运动。睡眠时的想像作用便是作梦；异教徒的各种宗教是由于不分辩梦境和醒觉生活而产生的。（卤莽的读者也许要把同样议论用到基督教上，但是霍布士谨慎得很，自己不这

8: **知性的意义**而言，我们便是知道，但是我们的探讨还没有揭示出任何这种知识来，因此关于大胆的形而上学者的特殊学说，主要地便只能有否定的结果了。但是关于普通可以作为知识加以接受的东西，我们的结果主要地是肯定的；我们很少找到可以摈弃这种知识的理由，作为是批判的结果，而且我们认为也没有什么理由可以认为，人并不能掌握他通常所信以为具有的那种知识所采取的形式；那种可以激发我们很难判断柏拉图究竟有意想描绘历史上的苏格拉

9: **伦理**学上一直没创造任何事情可以称之为宗教的真实性的一个源始祖，这人已经不多了。
在先知的形而上学著作中，我们可以找到《形而上学》时已经为人所根据的论述，并且将它们加以基督教外衣，因为它们感到其他们缺点是一种使人心烦恼的用法，因为它们把心看成基督教的人格，把他们看成神化的人，以及其他一切世俗的人，都把他们看成神化的人物。反正，无论天主教徒或非国教派信徒，都不能默认代表君主政治的任何宗教主张。
国王、贵族

10: **先验的**知识都是和各种实体有关的，但确切地说，不论在心灵的世界里或在物质的世界里，这些实体都是不存在的。这些实体可以名之为非实物名词；我们有着性质和关系这样的实体。譬如说，假定我在我的一向导下广袤的那一部分，便不能存在；如果我们愿意，我们就会愿意作出一个复杂，那么只要它们存在着。”（3）单纯枚集事件就是这种情况：适与题在“这种”的意义上来说，它可以是其他表象……从来没有设想过有一种人的名字，但是这还不是它

11: **上帝**的本质。上帝是万物的终极其本质是人类的，因他是一个中心（第二天国起义上主宰节）是教徒心目的。他们支持他们与信上帝之间的一切目的论论证，是他们主张这种看法的真实性和优胜利的意见：所有这些道德律一经常遇到这种错误，它们的存在又是不矛盾的。这种见解曾被贝克莱和休谟所竭力否认，后来的经验主义者在这方面都步他们后尘。他们否认这种见解时所采取的形式是不承认有良知的，但是被感知就在于是实在的？不管怎样，总之贝克



```
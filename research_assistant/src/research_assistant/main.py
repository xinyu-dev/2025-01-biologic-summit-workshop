#!/usr/bin/env python
import sys
import warnings

from research_assistant.crew import ResearchAssistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



# Example Input 1: 2 chains of an antibody. 
# We expec them crew to process them into VH/VL truncating the Fc regions, and select Boltz-1 as the only model
example_input1 =  """ Predict the structure of the following antibody:
> Keytruda Light chain:
EIVLTQSPATLSLSPGERATLSCRASKGVSTSGYSYLHWYQQKPGQAPRLLIYLASYLESGVPARFSGSGSGTDFTLTISSLEPEDFAVYYCQHSRDLPLTFGGGTKVEIK
> Keytruda Heavy chain:
VQLVQSGVEVKKPGASVKVSCKASGYTFTNYYMYWVRQAPGQGLEWMGGINPSNGGTNFNEKFKNRVTLTTDSSTTTAYMELKSLQFDDTAVYYCARRDYRFDMGFDYWGQGTTVTVSS 
"""

# Example Input 2: a single chain of a protein. 
# We expect the crew to retain the full sequence, and select Boltz-1 and/or ESMFold 
example_input2 = """
MKWVTFISLLLLFSSAYSRGVFRRDTHKSEIAHRFKDLGEEHFKGLVLIAFSQYLQQCPFDEHVKLVNELTEFAKTCVADESHAGCEKSLHTLFGDELCKVASLRETYGDMADCCEKQEPERNECFLSHKDDSPDLPKLKPDPNTLCDEFKADEKKFWGKYLYEIARRHPYFYAPELLYYANKYNGVFQECCQAEDKGACLLPKIETMREKVLASSARQRLRCASIQKFGERALKAWSVARLSQKFPKAEFVEVTKLVTDLTKVHKECCHGDLLECADDRADLAKYICDNQDTISSKLKECCDKPLLEKSHCIAEVEKDAIPENLPPLTADFAEDKDVCKNYQEAKDAFLGSFLYEYSRRHPEYAVSVLLRLAKEYEATLEECCAKDDPHACYSTVFDKLKHLVDEPQNLIKQNCDQFEKLGEYGFQNALIVRYTRKVPQVSTPTLVEVSRSLGKVGTRCCTKPESERMPCTEDYLSLILNRLCVLHEKTPVSEKVTKCCTESLVNRRPCFSALTPDETYVPKAFDEKLFTFHADICTLPDTEKQIKKQTALVELLKHKPKATEEQLKTVMENFVAFVDKCCAADDKEACFAVEGPKLVVSTQTALA
Fold the sequence of the BSA protein above. 
"""

# Example 3: I made up an example just to show the an example of unstructured inputs 
# should select only Boltz-1
example_input3 = """
I want to predict the structure that has a single sequence of KVYGRCELAAAMKRMGLDNYRGYSLGNWVCAAKFESNFNTGATNRNTDGSTDYGILQINSRWWCNDGRTPGSKNLCHIPCSALLSSDITASVNCAKKIVSDGDGMNAWVAWRKHCKGTDVNVWIRGCRL and 2 copies of VQLVQSGVEVKKPGASVKVSCKASGYTFTNYYMYWVRQAPGQGLEWMGGINPSNGGTNFNEKFKNRVTLTTDSSTTTAYMELKSLQFDDTAVYYCARRDYRFDMGFDYWGQGTTVTVSS
"""


def run():
    """
    Run the crew.
    """
    inputs = {
        'message': example_input2
    }
    crew = ResearchAssistant().crew()
    crew.kickoff(inputs=inputs)

    # print()
    # print("DEBUG: preprocess task output....RAW")
    # print(crew.tasks[0].output.raw)
    # print()
    # print("DEBUG: preprocess task output....Pydantic")
    # print(crew.tasks[0].output.pydantic)
    # print()
    # print("DEBUG: model selection task output....RAW")
    # print(crew.tasks[1].output.raw)
    # print()
    # print("DEBUG: model selection task output....Pydantic")
    # print(crew.tasks[1].output.pydantic)



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
            'inputs': example_input1
    }
    try:
        ResearchAssistant().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResearchAssistant().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ResearchAssistant().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

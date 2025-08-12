#!/usr/bin/env python3
# coding=utf-8
# Author: Alberto Olivares Alarcos <aolivares@iri.upc.edu>, Institut de Robòtica i Informàtica Industrial, CSIC-UPC
"""
code to generate explanations from ontology-based narratives using language models 
(in this code, an agent from pydantic-ai is used)
"""

from src.utils_module import utilsModule
from src.pydanticai_module import *

import time


system_prompt = "You are an agent that based on a given ontology-based narrative, shall provide a new narrative that: \
    (a) uses an easier language than the original, (b) is shorter than the original, and (c) keeps the semantic meaning \
    of the original. "

#system_prompt = "You are an agent that shall solve a {task}."

# user_prompt = "{task} : Based on a given ontology-based narrative, shall provide a new narrative that: (a) uses an easier \
#     language than the original, (b) is shorter than the original, and (c) keeps the semantic meaning of the original."



if __name__ == "__main__":
    start_time = time.time()

    utils_object = utilsModule()
    model_to_run = 'qwen3:8b' # qwen3:14b  |  qwen3:8b  |  qwen3:1.7b  |  gpt-oss:20b  
    narratives_csv_file = "generated_c_narratives_multiple_plans_comparison_with_specificity_1_dataset_unknown.csv"

    narratives_dict = utils_object.create_dict_from_csv_file(\
        utils_object.csv_file_path + "/explanatory_narratives_cra/acxon_based", \
        narratives_csv_file, ",")

    for i in range (0, 2):    
        user_prompt = narratives_dict["Explanation"][i]
        complete_user_prompt = user_prompt 

        ollama_model = OpenAIModel(
        model_name=model_to_run, provider=OpenAIProvider(base_url='http://localhost:11434/v1')
        )
        
        explanation_generation_agent = Agent(ollama_model, output_type=OntologyBasedExplanationOutput, system_prompt=system_prompt)
        #explanation_generation_agent = Agent(ollama_model, output_type=str, system_prompt=system_prompt) # it returns the complete text (as using the chat) good for debugging 
        #explanation_generation_agent = Agent(ollama_model, output_type=Union[OntologyBasedExplanationOutput, str], system_prompt=system_prompt) # it returns the text (Union uses smart mode by default)

        result = explanation_generation_agent.run_sync(complete_user_prompt)
        final_time = time.time()
        print('Result: ', result.output)
        #print('New explanation: ', type(result.output))
        #print('New explanation: ', result.output.narrative)

        elapsed_time = final_time - start_time
        print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

        """
        print(result.usage())
        ->
        Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)
        """
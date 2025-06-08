import re
import numpy as np
from sentence_transformers import SentenceTransformer
# Spotify 비교 string : NewJeans How Sweet official
# Youtube 비교 get_name의 response : NewJeans  How Sweet Official MV
def get_name(data):
  result = data['items'][0]['snippet']['title']
  return result

def replace_special(data):
  result = re.sub(r'[^ A-Za-z]', '', data)
  return result

class get_similarity:
  def __init__(self):
    self.client = SentenceTransformer('jhgan/ko-sroberta-multitask')

  def get_embedding(self, text):
    return self.client.encode(text)

  def cosine_similarity(self,a, b):
    dot_product = np.dot(a, b)

    # 각 벡터의 크기 계산
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # cosine similarity
    similarity = dot_product / (norm_a * norm_b)
    return similarity

  def cosine_distance(self, a, b):
    similarity = self.cosine_similarity(a, b)
    distance = 1 - similarity
    return distance
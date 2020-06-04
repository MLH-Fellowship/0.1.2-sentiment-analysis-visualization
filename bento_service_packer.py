from bento_service import SentimentClassifierService

bento_svc = SentimentClassifierService()
bento_svc.pack('model/model', model)
bento_svc.pack('word_index', word_index)

# 3) save your BentoSerivce
saved_path = bento_svc.save()

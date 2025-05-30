
from semantic_router.routers import SemanticRouter



from semantic_router import Route
# , RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    # utterances=[
    #     "What is the return policy of the products?",
    #     "Do I get discount with the HDFC credit card?",
    #     "How can I track my order?",
    #     "What payment methods are accepted?",
    #     "How long does it take to process a refund?",
    # ],
    utterances=["How does retimer work?"              
     "Who can benefit from retimer?"                         
     "When do I wear it?"                    
     "How do I know it works?"    
     "How long does it take to start working?","when do i wear?"],
    score_threshold=0.4
)
# faq = Route(
#     name='faq',
#     utterances=[
#         "What is the return policy of the products?",
#         "How long does it take to process a refund?",
#         "Can I get a refund?",
#         "What's your refund policy?",
#         "Do you offer refunds?",
#     ]
# )


sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ],
    score_threshold=0.4
)

# created a the route for small talk and added it in the routee layer
small_talk = Route(
    name='small-talk',
    utterances=[
        "How are you?",
        "What is your name?",
        "Are you a robot?",
        "What are you?",
        "What do you do?",
    ],
    score_threshold=0.4
)
routes=[faq, sql, small_talk]
# import pdb;pdb.set_trace()
semantics_router = SemanticRouter(routes=routes, encoder=encoder,auto_sync="local")
# semantics_router.prepare()
if __name__ == "__main__":
    print(semantics_router("what is your refund policy?").name,semantics_router("what is your refund policy?"))
    print(semantics_router("Pink Puma shoes in price range 5000 to 1000").name)
    print(semantics_router("How are you?").name)
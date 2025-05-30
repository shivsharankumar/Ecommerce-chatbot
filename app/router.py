
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
    utterances=["How does retimer work?",
                "Who can benefit from retimer?",
                "When do I wear it?",
                "How do I know it works?",
                "How long does it take to start working?",
                "Can I use the device more than once a day?",
                "Can I read or work while using retimer?",
                "Can I drive while using retimer?",
                "Can I shower while using retimer?",
                "Can I wear retimer outside?",
                "Where can I get the retimer mobile app?",
                "Who benefits from retimer?",
                "When do I wear it?",
                "Why is the light blue-green?",
                "Once charged, how long will it last?",
                "Can I wear them while they are charging?",
                "Who shouldn’t use retimer?",
                "Is the light source safe for the eyes?",
                "Once I use retimer, will my body clock be back on track permanently?",
                "Are there specific tips to improve the use/results of retimer?",
                "Do you have more information on how light therapy works?",
                "How does retimer compare to a light box?",
                "Do I need to pay import duties or taxes?",
                "I suffer from an eye condition, can I use retimer?",
                "I am on a light-sensitive (photosensitizing) medication, is it okay for me to use the light?",
                "Does retimer come with a carry case?",
],
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
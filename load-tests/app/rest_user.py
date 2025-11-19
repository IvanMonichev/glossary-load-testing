from locust import HttpUser, task, between
import random
from config import REST_HOST, TERM_IDS


class RestUser(HttpUser):
    wait_time = between(0.1, 0.5)
    host = REST_HOST

    @task(7)
    def get_term(self):
        term_id = random.choice(TERM_IDS)
        self.client.get(f"/terms/{term_id}", name="REST: GetTerm")

    @task(3)
    def search_terms(self):
        query = random.choice(["a", "e", "data", "tech"])
        page = random.randint(1, 5)

        self.client.get(
            f"/terms?query={query}&page={page}&page_size=20",
            name="REST: SearchTerms"
        )

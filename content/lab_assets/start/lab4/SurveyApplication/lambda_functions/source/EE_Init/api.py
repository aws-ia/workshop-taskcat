import urllib.parse
import requests


class EEAPIClient:

  def __init__(self, api_base, api_token, game_id, module_id):
    self.api_base = api_base
    self.api_token = api_token
    self.game_id = game_id
    self.module_id = module_id

  def get_all_teams(self):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams")
    for x in range(0,5):
      if x > 0:
        print("Get all teams retry: {}".format(x))
      try:
        r = requests.get(url, headers=self._get_headers(), timeout=5)
        break
      except Exception as err:
        print(err)
    return r.json()['teams']

  def get_one_team(self, team_id):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}")
    r = requests.get(url, headers=self._get_headers(), timeout=5)
    return r.json()

  def set_checkpoint(self, team_id, checkpoint):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/modules/{self.module_id}/checkpoints")
    requests.post(url, json={
      "checkpoint": checkpoint
    }, headers=self._get_headers(), timeout=5)
    return

  def points(self, team_id, points, reason=""):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/score")
    body = {
      "type": "points",
      "value": points,
      "reason": reason
    }
    for x in range(0, 5):
      if x > 0:
        print("Points retry: {}".format(x))
      try:
        requests.post(url, json=body, headers=self._get_headers(), timeout=5)
        break
      except Exception as err:
        print(err)
    return

  def points_ppm(self, team_id, weight, reason):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/score")
    body = {
      "type": "ppm",
      "value": weight,
      "reason": reason
    }
    for x in range(0, 5):
      if x > 0:
        print("PPM retry: {}".format(x))
      try:
        requests.post(url, json=body, headers=self._get_headers(), timeout=5)
        break
      except Exception as err:
        print(err)
    return

  def get_input(self, team_id, key):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/modules/{self.module_id}/inputs/{key}")
    r = requests.get(url, headers=self._get_headers(), timeout=5)
    return r.json()

  def post_input(self, team_id, key, label, description=""):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/modules/{self.module_id}/inputs")
    requests.post(url, json={
      "key": key,
      "label": label,
      "description": description
    }, headers=self._get_headers(), timeout=5)
    return

  def post_output(self, team_id, key, label, value, dashboard_index, markdown=False, description=""):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/modules/{self.module_id}/outputs")
    requests.post(url, json={
      "key": key,
      "label": label,
      "value": value,
      "description": description,
      "markdown": markdown,
      "dashboard-index": dashboard_index
    }, headers=self._get_headers(), timeout=5)
    return

  def get_config(self, team_id, key):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/modules/{self.module_id}/config/{key}")
    r = requests.get(url, headers=self._get_headers(), timeout=5)
    return r.json()

  def set_config(self, team_id, key, value):
    url = urllib.parse.urljoin(self.api_base, f"games/{self.game_id}/teams/{team_id}"
                                              f"/modules/{self.module_id}/config")
    requests.post(url, json={
      "key": key,
      "value": value,
    }, headers=self._get_headers(), timeout=5)
    return

  def _get_headers(self):
    return { 
      'Authorization': f'Bearer {self.api_token}', 
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    }
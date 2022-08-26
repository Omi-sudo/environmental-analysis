"""
secrets_util.py
This is the utility module to access
the secrets stored in gcp environment.
"""

import logging
import traceback

from google.cloud import secretmanager_v1

logging.basicConfig(level=logging.INFO)

def access_secrets(secret_names):
  """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
  """

  try:

    client = secretmanager_v1.SecretManagerServiceClient()
    response = client.access_secret_version(name=secret_names)
    payload = response.payload.data.decode("UTF-8")
    return payload

  except Exception as exception:
    logging.error("An exception occurred in [access_secrets]")
    logging.error("Exception occurred due to %s",str(exception))
    logging.error(traceback.print_exc())
    raise Exception(traceback.print_exc()) from exception

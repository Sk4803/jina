import requests

from ..models import DaemonID
from .containers import ContainerStore
from ..excepts import Runtime400Exception


class FlowStore(ContainerStore):
    _kind = 'flow'

    def _add(self, **kwargs):
        """Sends `post` request to `mini-jinad` to create a Flow."""
        try:
            params = {'filename': self.params['uses'], 'id': self.params['identity']}
            if 'port_expose' in kwargs:
                params.update({'port_expose': kwargs['port_expose']})

            r = requests.post(url=f'{self.host}/{self._kind}', params=params)
            if r.status_code != requests.codes.created:
                raise Runtime400Exception(f'Flow creation failed {r.json()}')
        except requests.exceptions.RequestException as ex:
            self._logger.error(f'{ex!r}')
            raise

    def _update(self):
        try:
            # TODO
            r = requests.post(url=f'{self.host}/{self._kind}')
        except requests.exceptions.RequestException as ex:
            raise

    def _delete(self):
        """Sends `delete` request to `mini-jinad` to terminate a Flow."""
        try:
            r = requests.delete(url=f'{self.host}/{self._kind}')
            if r.status_code != requests.codes.ok:
                self._logger.critical(f'')
                raise Runtime400Exception(f'Flow deletion failed {r.json()}')
        except requests.exceptions.RequestException as ex:
            raise

    def update(self, id: DaemonID) -> DaemonID:
        # TODO
        pass
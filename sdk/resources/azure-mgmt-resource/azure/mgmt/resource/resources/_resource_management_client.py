# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import ResourceManagementClientConfiguration



class ResourceManagementClient(MultiApiClientMixin, SDKClient):
    """Provides operations for working with resources and resource groups.

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: ResourceManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2019-05-10'
    _PROFILE_TAG = "azure.mgmt.resource.resources.ResourceManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = ResourceManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ResourceManagementClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-02-01: :mod:`v2016_02_01.models<azure.mgmt.resource.resources.v2016_02_01.models>`
           * 2016-09-01: :mod:`v2016_09_01.models<azure.mgmt.resource.resources.v2016_09_01.models>`
           * 2017-05-10: :mod:`v2017_05_10.models<azure.mgmt.resource.resources.v2017_05_10.models>`
           * 2018-02-01: :mod:`v2018_02_01.models<azure.mgmt.resource.resources.v2018_02_01.models>`
           * 2018-05-01: :mod:`v2018_05_01.models<azure.mgmt.resource.resources.v2018_05_01.models>`
           * 2019-05-01: :mod:`v2019_05_01.models<azure.mgmt.resource.resources.v2019_05_01.models>`
           * 2019-05-10: :mod:`v2019_05_10.models<azure.mgmt.resource.resources.v2019_05_10.models>`
        """
        if api_version == '2016-02-01':
            from .v2016_02_01 import models
            return models
        elif api_version == '2016-09-01':
            from .v2016_09_01 import models
            return models
        elif api_version == '2017-05-10':
            from .v2017_05_10 import models
            return models
        elif api_version == '2018-02-01':
            from .v2018_02_01 import models
            return models
        elif api_version == '2018-05-01':
            from .v2018_05_01 import models
            return models
        elif api_version == '2019-05-01':
            from .v2019_05_01 import models
            return models
        elif api_version == '2019-05-10':
            from .v2019_05_10 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def deployment_operations(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`DeploymentOperations<azure.mgmt.resource.resources.v2016_02_01.operations.DeploymentOperations>`
           * 2016-09-01: :class:`DeploymentOperations<azure.mgmt.resource.resources.v2016_09_01.operations.DeploymentOperations>`
           * 2017-05-10: :class:`DeploymentOperations<azure.mgmt.resource.resources.v2017_05_10.operations.DeploymentOperations>`
           * 2018-02-01: :class:`DeploymentOperations<azure.mgmt.resource.resources.v2018_02_01.operations.DeploymentOperations>`
           * 2018-05-01: :class:`DeploymentOperations<azure.mgmt.resource.resources.v2018_05_01.operations.DeploymentOperations>`
           * 2019-05-01: :class:`DeploymentOperations<azure.mgmt.resource.resources.v2019_05_01.operations.DeploymentOperations>`
           * 2019-05-10: :class:`DeploymentOperations<azure.mgmt.resource.resources.v2019_05_10.operations.DeploymentOperations>`
        """
        api_version = self._get_api_version('deployment_operations')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import DeploymentOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import DeploymentOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import DeploymentOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import DeploymentOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import DeploymentOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import DeploymentOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import DeploymentOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def deployments(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2016_02_01.operations.DeploymentsOperations>`
           * 2016-09-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2016_09_01.operations.DeploymentsOperations>`
           * 2017-05-10: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2017_05_10.operations.DeploymentsOperations>`
           * 2018-02-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2018_02_01.operations.DeploymentsOperations>`
           * 2018-05-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2018_05_01.operations.DeploymentsOperations>`
           * 2019-05-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_05_01.operations.DeploymentsOperations>`
           * 2019-05-10: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_05_10.operations.DeploymentsOperations>`
        """
        api_version = self._get_api_version('deployments')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import DeploymentsOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import DeploymentsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2018-05-01: :class:`Operations<azure.mgmt.resource.resources.v2018_05_01.operations.Operations>`
           * 2019-05-01: :class:`Operations<azure.mgmt.resource.resources.v2019_05_01.operations.Operations>`
           * 2019-05-10: :class:`Operations<azure.mgmt.resource.resources.v2019_05_10.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2018-05-01':
            from .v2018_05_01.operations import Operations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import Operations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def providers(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2016_02_01.operations.ProvidersOperations>`
           * 2016-09-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2016_09_01.operations.ProvidersOperations>`
           * 2017-05-10: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2017_05_10.operations.ProvidersOperations>`
           * 2018-02-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2018_02_01.operations.ProvidersOperations>`
           * 2018-05-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2018_05_01.operations.ProvidersOperations>`
           * 2019-05-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_05_01.operations.ProvidersOperations>`
           * 2019-05-10: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_05_10.operations.ProvidersOperations>`
        """
        api_version = self._get_api_version('providers')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import ProvidersOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import ProvidersOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def resource_groups(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2016_02_01.operations.ResourceGroupsOperations>`
           * 2016-09-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2016_09_01.operations.ResourceGroupsOperations>`
           * 2017-05-10: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2017_05_10.operations.ResourceGroupsOperations>`
           * 2018-02-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2018_02_01.operations.ResourceGroupsOperations>`
           * 2018-05-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2018_05_01.operations.ResourceGroupsOperations>`
           * 2019-05-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_05_01.operations.ResourceGroupsOperations>`
           * 2019-05-10: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_05_10.operations.ResourceGroupsOperations>`
        """
        api_version = self._get_api_version('resource_groups')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import ResourceGroupsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def resources(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2016_02_01.operations.ResourcesOperations>`
           * 2016-09-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2016_09_01.operations.ResourcesOperations>`
           * 2017-05-10: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2017_05_10.operations.ResourcesOperations>`
           * 2018-02-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2018_02_01.operations.ResourcesOperations>`
           * 2018-05-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2018_05_01.operations.ResourcesOperations>`
           * 2019-05-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_05_01.operations.ResourcesOperations>`
           * 2019-05-10: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_05_10.operations.ResourcesOperations>`
        """
        api_version = self._get_api_version('resources')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import ResourcesOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import ResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tags(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2016_02_01.operations.TagsOperations>`
           * 2016-09-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2016_09_01.operations.TagsOperations>`
           * 2017-05-10: :class:`TagsOperations<azure.mgmt.resource.resources.v2017_05_10.operations.TagsOperations>`
           * 2018-02-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2018_02_01.operations.TagsOperations>`
           * 2018-05-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2018_05_01.operations.TagsOperations>`
           * 2019-05-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_05_01.operations.TagsOperations>`
           * 2019-05-10: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_05_10.operations.TagsOperations>`
        """
        api_version = self._get_api_version('tags')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import TagsOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import TagsOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import TagsOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import TagsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import TagsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import TagsOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import TagsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel
from registry.models.registration_status_category import RegistrationStatusCategory
from registry.models.workflow import Workflow
from community.models.profile import Profile



class ReviewRequestService(TimeStampedModel):
    service = models.ForeignKey('registry.Service', related_name='review_requests', verbose_name=_('service'))
    workflow = models.ForeignKey('registry.Workflow', related_name='review_requests', verbose_name=_('workflow'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    approved = models.BooleanField(default=False, verbose_name=_('approved'))

    class Meta:
        verbose_name=_('service review request')

    def approve(self):
        # self.approved = True
        # self.save()
        self.workflow.description = self.description
        self.workflow.reviewed = True
        self.workflow.save()
        new_state = RegistrationStatusCategory.objects.get(name=RegistrationStatusCategory.REGISTERED)
        self.save_workflow(new_state)

    def disapprove(self):
        self.workflow.description = self.description
        self.workflow.reviewed = True
        self.workflow.save()
        new_state = RegistrationStatusCategory.objects.get(name=RegistrationStatusCategory.DRAFT)
        self.save_workflow()

    def save_workflow(self, new_state):
        # TODO: get logged author
        author = self.workflow.author
        workflow = Workflow.objects.create(
                               author=author,
                               old_state=self.workflow.new_state,
                               new_state=new_state,
                               previous_node=self.workflow,
                               reviewed=True)
        workflow.save()
        self.service.workflow = workflow
        self.service.registration_status = new_state
        self.service.save()

    def __str__(self):
        return _('Review service {service} by {author} ({modified})').format(service=self.service.name, author=self.workflow.author, modified=self.modified)

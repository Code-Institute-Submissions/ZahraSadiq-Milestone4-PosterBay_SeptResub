from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook from Stripe """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean data in the shipping details 
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        try: 
            order = Order.objects.get(
                first_name__iexact=shipping_details.name,
                email__iexact=shipping_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.country,
                streetaddress__iexact=shipping_details.line1,
                house_number__iexact=shipping_details.line2,
                city__iexact=shipping_details.city,
                grand_total= grand_total,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already stored',
                status=200)
        except Order.DoesNotExist:
            try:

                order = Order.objects.create(
                    first_name=shipping_details.name,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.country,
                    streetaddress=shipping_details.line1,
                    house_number=shipping_details.line2,
                    city=shipping_details.city,
                    grand_total= grand_total,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
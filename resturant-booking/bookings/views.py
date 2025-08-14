from django.shortcuts import render

# Create your views here.from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.order_by('-date','-time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})

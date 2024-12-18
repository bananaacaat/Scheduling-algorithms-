from django.shortcuts import render
from django.http import JsonResponse
import json
from scheduling_algorithms import fcfs, sjf, rm, dm, llf, edf
import matplotlib.pyplot as plt
import os
from django.conf import settings

# Main page view
def index(request):
    return render(request, 'scheduler/index.html')

def generate_gantt_chart(schedule):
    """
    Generate a Gantt chart for the given schedule and save it to the media directory.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    for task in schedule:
        ax.barh(task['task'], task['end'] - task['start'], left=task['start'], height=0.5, color='skyblue')

    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('Gantt Chart for Task Scheduling')
    ax.grid(True)

    chart_path = os.path.join(settings.MEDIA_ROOT, 'gantt_chart.png')
    plt.savefig(chart_path)
    plt.close()
    return os.path.join(settings.MEDIA_URL, 'gantt_chart.png')


def simulate(request):
    if request.method == 'POST':
        algorithm = request.POST.get('algorithm')

        # Construire les tâches à partir des champs individuels
        task_ids = request.POST.getlist('task_id')
        arrival_times = request.POST.getlist('arrival_time')
        execution_times = request.POST.getlist('execution_time')
        deadlines = request.POST.getlist('deadline')
        periods = request.POST.getlist('period')

        tasks = [
            {
                "id": int(task_ids[i]),
                "arrival_time": int(arrival_times[i]),
                "execution_time": int(execution_times[i]),
                "deadline": int(deadlines[i]),
                "period": int(periods[i]),
            }
            for i in range(len(task_ids))
        ]

        # Sélectionner l'algorithme
        if algorithm == 'FCFS':
            result, steps = fcfs(tasks)
        elif algorithm == 'SJF':
            result, steps = sjf(tasks)
        elif algorithm == 'RM':
            result, steps = rm(tasks)
        elif algorithm == 'DM':
            result, steps = dm(tasks)
        elif algorithm == 'LLF':
            result, steps = llf(tasks)
        elif algorithm == 'EDF':
            result, steps = edf(tasks)
        else:
            result, steps = [], ["Invalid algorithm"]

        # Générer le diagramme de Gantt
        chart_path = generate_gantt_chart(result)

        return render(request, 'scheduler/simulate.html', {
            'result': "\n".join([f"Task {t['task']} - Start: {t['start']}, End: {t['end']}" for t in result]),
            'steps': "\n".join(steps),
            'gantt_chart': chart_path,
        })
    return render(request, 'scheduler/simulate.html')

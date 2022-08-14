import os

def delete_samples_cron_job():
    samples_directory = "spa/static/samples"
    for sample in os.listdir(samples_directory):
        os.remove(os.path.join(samples_directory, sample))
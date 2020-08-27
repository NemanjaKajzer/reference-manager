import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';


const httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };

@Injectable({
    providedIn: 'root'
})
export class ReferenceService {
    private requestUrl: string;

    constructor(private http: HttpClient) { }


    public save(file) {
        return this.http.post('/server/upload/', file);
    }

}
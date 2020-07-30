import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';





const httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };

@Injectable({
    providedIn: 'root'
})
export class AuthenticationService {
    private requestUrl: string;

    constructor(private http: HttpClient) { }


    public login(authentication) {
        return this.http.post('/server/auth/', authentication);
    }

    public logOut() {
        console.log('Logged out successfully');
        this.requestUrl = '/server/authentication/logout';
        return this.http.get<string>(this.requestUrl, httpOptions);
    }
}
